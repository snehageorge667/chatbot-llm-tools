from langgraph.graph import StateGraph, END
from typing import TypedDict

from .llm_node import llm_node
from .tool_node import tool_node


# ---- State (chat memory preserved) ----
class ChatState(TypedDict):
    message: str
    response: str


# ---- Build graph ----
builder = StateGraph(ChatState)

builder.add_node("llm", llm_node)
builder.add_node("tools", tool_node)

# Flow:
# user -> LLM -> tools -> END
builder.set_entry_point("llm")
builder.add_edge("llm", "tools")
builder.add_edge("tools", END)

# ---- Compile ----
chat_graph = builder.compile()
