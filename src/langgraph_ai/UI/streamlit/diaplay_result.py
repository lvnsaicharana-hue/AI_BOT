import streamlit as st
from langchain_core.messages import HumanMessage


class DisplayResultStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):

        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

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