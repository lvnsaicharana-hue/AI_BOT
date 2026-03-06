import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):

        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        # -------- BASIC CHATBOT --------
        if usecase.lower() == "basic chatbot":

            # display user message
            with st.chat_message("user"):
                st.write(user_message)

            # run the graph
            for event in graph.stream({
                "messages": [HumanMessage(content=user_message)]
            }):

                for value in event.values():

                    response = value["messages"][-1]

                    with st.chat_message("assistant"):
                        st.write(response.content)

        # -------- CHATBOT WITH WEB TOOL --------
        elif usecase.lower() == "chatbot with tool":

            # Prepare initial state
            initial_state = {
                "messages": [HumanMessage(content=user_message)]
            }

            # Run the graph
            res = graph.invoke(initial_state)

            for message in res["messages"]:

                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)

                elif isinstance(message, ToolMessage):
                    with st.chat_message("assistant"):
                        st.write("🔧 Tool Call Start")
                        st.write(message.content)
                        st.write("🔧 Tool Call End")

                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)