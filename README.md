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
