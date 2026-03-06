from src.langgraph_ai.state.state import State
from langchain_core.messages import HumanMessage


class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Processes the input and generate the response with tool integration
        """

        messages = state["messages"]

        # invoke LLM with correct message format
        response = self.llm.invoke(messages)

        return {"messages": [response]}