import os
from typing import  List
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, BaseMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from models.code_info_model import CodeInfoModel
from constants.constants import Constants

class LLMChainService:
    def __init__(self, openai_api_key):
        self.__llm_chain = ChatOpenAI(api_key=openai_api_key)
    
    def format_chat_message(self, code_info: CodeInfoModel) -> List[BaseMessage]:
        chat_template = self.__create_chat_prompt_template()
        return chat_template.format_messages(
                problem_heading=code_info.problem_heading, 
                description=code_info.description,
                lang=code_info.lang,
                code=code_info.code
            )
    
    def invoke(self, messages:List[BaseMessage]) -> str:
        output = self.__llm_chain.invoke(messages)
        return output.content
    
    def __create_chat_prompt_template(self) -> ChatPromptTemplate:
        return ChatPromptTemplate.from_messages([
            self.__get_system_message(),
            self.__get_human_message_template()
        ])
    
    def __get_system_message(self) -> SystemMessage:
        return SystemMessage(content=self.__get_system_message_prompt())

    def __get_human_message_template(self) -> HumanMessagePromptTemplate:
        return HumanMessagePromptTemplate.from_template(self.__get_human_message_prompt())

    def __get_human_message_prompt(self) -> str:
        human_msg_prompt = ""
        file_path = os.path.join(Constants.BASE_FILE_PATH, Constants.HUMAN_MSG_FILE_NAME)
        with open(file_path, 'r') as f:
            human_msg_prompt = f.read()
        return human_msg_prompt

    def __get_system_message_prompt(self) -> str:
        sys_msg_prompt = ""
        file_path = os.path.join(Constants.BASE_FILE_PATH, Constants.SYS_MSG_FILE_NAME)
        with open(file_path, 'r') as f:
            sys_msg_prompt = f.read()
        return sys_msg_prompt


    
