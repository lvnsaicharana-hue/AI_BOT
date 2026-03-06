import os
from configparser import ConfigParser


class Config:

    def __init__(self):
        self.config = ConfigParser()

        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, "uiconfi.ini")

        self.config.read(config_path)

    def get_llm_options(self):
        value = self.config.get("DEFAULT", "LLM_OPTIONS")
        return [x.strip() for x in value.split(",")]

    def get_usecase_options(self):
        value = self.config.get("DEFAULT", "USECASE_OPTIONS")
        return [x.strip() for x in value.split(",")]

    def get_groq_model_options(self):
        value = self.config.get("DEFAULT", "GROQ_MODEL_OPTIONS")
        return [x.strip() for x in value.split(",")]

    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE")