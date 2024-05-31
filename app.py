import gradio as gr
from utils import get_doc_tools
from get_agent import agent_with_reasoning_loop

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

import os
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
Settings.llm = Ollama(base_url=ollama_base_url,model='llama3',request_timeout=3600.0,temperature=1)
Settings.embed_model = OllamaEmbedding(base_url=ollama_base_url, model_name='nomic-embed-text')

def create_agent(uploaded_pdf,session_state):
    vector_tool, summary_tool = get_doc_tools(uploaded_pdf)
    tools = [vector_tool, summary_tool]
    agent = agent_with_reasoning_loop(tools,Settings.llm)
    print("agent created")
    return {input_box: gr.Textbox(value="Ask a question", visible=True),
            state_var:[agent]}

def response_generator(text,session_state):
    print("Query: ",text)
    agent = session_state[0]
    response = agent.stream_chat(text)
    response_gen = response.response_gen
    output = ""
    for token in response_gen:
        output+=token
        yield {output_box:output}

def submit():
    return {input_box: gr.Textbox(visible=True)}

with gr.Blocks() as demo:

    gr.Markdown(
    """
    # Phi3 3.8B

    ## Agentic RAG with Reasoning Loop

    - ***LLM:*** Phi3 Mini
    - ***Embedding:*** nomic-embed-text
    - ***Framework:*** Llama Index 

    """)
    
    state_var = gr.State([])

    with gr.Row():
        upload_button = gr.UploadButton("📁 Upload PDF", file_types=[".pdf"])
    error_box = gr.Textbox(label="Error", visible=False)

    input_box = gr.Textbox(autoscroll=True,visible=False,label='User')
    output_box = gr.Textbox(autoscroll=True,max_lines=30,value="Output",label='Assistant')
    gr.Interface(fn=response_generator, inputs=[input_box,state_var], outputs=[output_box,state_var])
    upload_button.upload(create_agent,inputs=[upload_button,state_var],outputs=[input_box,state_var],queue=True,show_progress=True,trigger_mode="once")
    upload_button.upload(submit,None,input_box)
    
demo.queue()
demo.launch()


