import streamlit as st
from src.langgraph_ai.UI.streamlit.loadui import LoadStreamlitUI
from src.langgraph_ai.graph.grap_builder import GraphBuilder
from src.langgraph_ai.LLMs.groqllm import GroqLLM
from src.langgraph_ai.UI.streamlit.diaplay_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load input from UI.")
        return

    # CHAT INPUT BOX
    user_message = st.chat_input("Type your message...")

    if user_message:
        try:

            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("LLM model not initialized")
                return

            usecase = user_input.get("selected_usecase")

            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usecase)

            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

        except Exception as e:
            st.error(f"Graph setup failed: {e}")