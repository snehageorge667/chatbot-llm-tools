from backend.tools.greeting_tool import greeting_tool
from backend.tools.search_tool import search_tool
from backend.tools.fallback_tool import fallback_tool


def tool_node(state: dict) -> dict:
    user_msg = state["message"].lower()

    if any(word in user_msg for word in ["hi", "hello", "hey"]):
        response = greeting_tool(user_msg)
    elif "search" in user_msg:
        response = search_tool(user_msg)
    else:
        response = fallback_tool(user_msg)

    return {
        "message": state["message"],
        "response": response
    }
