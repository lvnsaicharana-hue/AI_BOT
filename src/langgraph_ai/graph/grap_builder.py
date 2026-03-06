from langgraph.graph import StateGraph, START, END
from src.langgraph_ai.state.state import State
from src.langgraph_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_ai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraph_ai.tools.search_tool import get_tools, create_tool_node


class GraphBuilder:

    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def build_basic_chatbot(self):

        chatbot = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", chatbot.process)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def build_chatbot_with_tool(self):

        tools = get_tools()

        chatbot = ChatbotWithToolNode(self.llm)
        tool_node = create_tool_node(tools)

        self.graph_builder.add_node("chatbot", chatbot.process)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", "tools")
        self.graph_builder.add_edge("tools", END)

    def setup_graph(self, usecase):

        if usecase.lower() == "basic chatbot":
            self.build_basic_chatbot()

        elif "tool" in usecase.lower():
            self.build_chatbot_with_tool()

        return self.graph_builder.compile()