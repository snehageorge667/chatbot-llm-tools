from backend.graph.llm_node import llm_node
from backend.memory.chat_memory import ChatMemory

memory = ChatMemory()

async def route_message(user_input: str):
    memory.add_message("user", user_input)
    reply = await llm_node["run"](user_input, memory.get_history())
    memory.add_message("assistant", reply)
    return reply
