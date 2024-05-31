# Reasoning-AGENT
Simple agents are good for 1-to-1 retrieval system. For more complex task we need multi steps reasoning loop.  In a reasoning loop the agent can break down a complex task into subtasks and solve them step by step while maintaining a conversational memory.


# Intoduction
In the our previous [`WORK`](https://github.com/swastikmaiti/AGENTIC-RAG.git), we have discussed about what is an agent and how AGENTIC-RAG works. 
A simple Agentic-RAG is good for 1-to-1 question answering. However a complex task may requiire sequence of subtasks to be executed to arrive at
the final answer. This is where reasoning loop comes into play. In a reasoning loop the agent is able to perform subtaks sequentially until final 
response. 

A agent consist of Agent Runner and Agent Worker. These two componnt interact in a cyclic manner until final response. Agent worker perform
the actual work of tool selection through reasoning via chain of thoughts and deciding next step or formulating the final output. Whereas Agent Runner
is the orechastator responsible for mainintaining task state and memory buffer. It works more like a scheduler and dispatcher.

The Image below shows the Agent Reasoning Loop with Agent Component and their role.


<img src="https://github.com/swastikmaiti/Reasoning-AGENT/blob/114af6cab5a4823d7b5ee065525c21cda933abdd/agent_reasoning_loop.png" height="500" width="500" >  

`image refernec:`[`DeepLearning.AI`](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/?utm_campaign=llamaindexC2-launch&utm_medium=headband&utm_source=dlai-homepage)

# Control Flow

On a broader term the Reasoning Loop perform tasks in a logical sequence. Well what is the sequence. How every component is interacting?

To understand the workflow we need to undestand chain of thoughts. To break a complex task into subtask LlamaIndex Agent makes use of chain 
of thought to guide the LLM into deciding the next action. These chain of thought are introduced by template with some fixed set of prompts and some 
dymanic context relevant to the current step.

The diagram below shows the sequence of events in an `AGENT REASONING LOOP`

<img src="https://github.com/swastikmaiti/Reasoning-AGENT/blob/114af6cab5a4823d7b5ee065525c21cda933abdd/agent_reasoning_loop_controlflow.png" height="500" width="800" >


# Frameworks
- ***Agentic-RAG:*** Llama Index
- ***App:*** Gradio
- ***LLM:*** Llama3 8B
- ***Embedding:*** nomic-embed-text
- ***Local LLM:*** Ollama
- ***Containerization:*** Docker

# File Structure
- agent-reasoning-loop.ipynb: Code for implementing an RAG Agent with Llama Index.
- app.py: Code Gradio application. Tools creation functions are present in `utils.py` and AGENT creation funtions are present in `get_agent.py`

# How to RUN
We need a LINUX system with atleast 8GB RAM.
- Install libraries with `make install`
- To Run the Application execute `docker compose up`
If you want to run the notebooks
- Download Ollama Docker Image and start Ollama server with `ollama_docker` on a new CLI as the server will block the CLI.
- Now `agent-reasoning-loop.ipynb` Notebook can be executed.
If previous images or container exist with same name it may create conflict. Delete image/conatiners if name conflict occurs.

# References
- [`LlamaIndex`](https://docs.llamaindex.ai/en/stable/)
- [`DeepLearning.AI`](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/?utm_campaign=llamaindexC2-launch&utm_medium=headband&utm_source=dlai-homepage)

# Acknowledgements
- Thanks to DeepLearning.AI and LlamaIndex for the wonderful [course](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/?utm_campaign=llamaindexC2-launch&utm_medium=headband&utm_source=dlai-homepage)
- Thanks to `Meta` for open source Llama3
#
### If you find the repo helpful, please drop a ⭐

