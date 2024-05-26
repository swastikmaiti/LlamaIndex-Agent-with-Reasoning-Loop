"""Create LlamaIndex Tools"""

from llama_index.core import SimpleDirectoryReader,Settings,VectorStoreIndex, SummaryIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.vector_stores import MetadataFilters, FilterCondition
from typing import List

def get_doc_tools(
        file_path: str
)->str:
    """get vector query tool and summary tool from a document"""

    #Load document
    document = SimpleDirectoryReader(input_files=[file_path]).load_data()
    name = document[0].metadata['file_name'].split('.')[0]
    splitter = SentenceSplitter(chunk_size=512,chunk_overlap=64)
    nodes = splitter.get_nodes_from_documents(documents=document)

    #Build vector query tool
    vector_index = VectorStoreIndex(nodes=nodes)
    vector_query_engine = vector_index.as_query_engine(similarity_top_k=2)

    vector_query_tool = QueryEngineTool.from_defaults(
        name=f"vector_tool_{name}",
        query_engine=vector_query_engine,
        description=(
            "Useful for specific topic based questions"
            "Do NOT use if you need a summary of the document."
        )
    )
    summary_index = SummaryIndex(nodes[:3])
    summary_query_engine = summary_index.as_query_engine(
        response_mode="tree_summarize"
    )
    summary_tool = QueryEngineTool.from_defaults(
        name=f"summary_tool_{name}",
        query_engine=summary_query_engine,
        description=(
            "Use ONLY IF you want to get a summary of the document. "
            "Do NOT use if you have specific questions related to document."
        )
    )

    return vector_query_tool, summary_tool