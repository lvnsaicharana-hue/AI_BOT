from langgraph.graph import StateGraph, START, END
from src.langgraph_ai.state.state import State
from src.langgraph_ai.nodes.basic_chatbot_node import BasicChatbotNode


class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def build_basic_chatbot_graph(self):

        chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node(
            "chatbot",
            chatbot_node.process
        )

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):

        if usecase.lower() == "basic chatbot":
            self.build_basic_chatbot_graph()

        return self.graph_builder.compile()