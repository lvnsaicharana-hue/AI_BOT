from src.langgraph_ai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        process the input state
        """

        response = self.llm.invoke(state["messages"])

        return {
            "messages": [response]
        }