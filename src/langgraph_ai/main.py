import streamlit as st

from src.langgraph_ai.UI.streamlit.loadui import LoadStreamlitUI
from src.langgraph_ai.graph.grap_builder import GraphBuilder
from src.langgraph_ai.LLMs.groqllm import GroqLLM
from src.langgraph_ai.UI.streamlit.diaplay_result import DisplayResultStreamlit

# IMPORT TOOLS
from src.langgraph_ai.tools.search_tool import get_tools, create_tool_node


def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load input from UI.")
        return

    # Chat input
    user_message = st.chat_input("Type your message...")

    if user_message:
        try:

            # Initialize LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("LLM model not initialized")
                return

            # Selected usecase
            usecase = user_input.get("selected_usecase")

            graph_builder = GraphBuilder(model)

            # 🔹 TOOL CHATBOT
            if usecase.lower() == "chatbot with tool":

                tools = get_tools()
                tool_node = create_tool_node(tools)

                graph = graph_builder.setup_graph(usecase)

            # 🔹 BASIC CHATBOT
            else:

                graph = graph_builder.setup_graph(usecase)

            # Display result
            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

        except Exception as e:
            st.error(f"Graph setup failed: {e}")

            

