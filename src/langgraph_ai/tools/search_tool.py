from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode
def get_tools():
    """
    Return the list of tools
    """
    tools=[TavilySearchResults(max_results=2)]
    return tools
def create_tool_node(tools):
    """
    create the tool node for graph
    """
    return ToolNode(tools=tools)