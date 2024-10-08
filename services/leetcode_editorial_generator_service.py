import os
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, BaseMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from models.code_info_model import CodeInfoModel
from constants.constants import Constants

class LeetcodeEditorialGeneratorService:
    """
    A service class to generate Leetcode editorials using OpenAI's language model.
    """

    def __init__(self, openai_api_key: str):
        """
        Initializes the service with the given OpenAI API key.
        
        Args:
            openai_api_key (str): The API key for accessing OpenAI services.
        """
        self.__llm_chain = ChatOpenAI(
            model=Constants.GPT_MODEL,
            api_key=openai_api_key
        )
    
    def format_chat_message(self, code_info: CodeInfoModel) -> List[BaseMessage]:
        """
        Formats the chat messages based on the provided code information.
        
        Args:
            code_info (CodeInfoModel): The model containing code information.
        
        Returns:
            List[BaseMessage]: A list of formatted chat messages.
        """
        chat_template = self.__create_chat_prompt_template()
        return chat_template.format_messages(
            problem_heading=code_info.problem_heading, 
            description=code_info.description,
            lang=code_info.lang,
            code=code_info.code
        )
    
    def invoke(self, messages: List[BaseMessage]) -> str:
        """
        Invokes the language model with the provided messages and returns the output.
        
        Args:
            messages (List[BaseMessage]): A list of messages to be sent to the language model.
        
        Returns:
            str: The content of the language model's response.
        """
        output = self.__llm_chain.invoke(messages)
        return output.content
    
    def __create_chat_prompt_template(self) -> ChatPromptTemplate:
        """
        Creates a chat prompt template using system and human messages.
        
        Returns:
            ChatPromptTemplate: The created chat prompt template.
        """
        return ChatPromptTemplate.from_messages([
            self.__get_system_message(),
            self.__get_human_message_template()
        ])
    
    def __get_system_message(self) -> SystemMessage:
        """
        Retrieves the system message for the chat prompt.
        
        Returns:
            SystemMessage: The system message object.
        """
        return SystemMessage(content=self.__read_message_prompt(Constants.SYS_MSG_FILE_NAME))

    def __get_human_message_template(self) -> HumanMessagePromptTemplate:
        """
        Retrieves the human message template for the chat prompt.
        
        Returns:
            HumanMessagePromptTemplate: The human message template object.
        """
        return HumanMessagePromptTemplate.from_template(self.__read_message_prompt(Constants.HUMAN_MSG_FILE_NAME))

    def __read_message_prompt(self, file_name: str) -> str:
        """
        Reads and returns the message prompt from a file.
        
        Args:
            file_name (str): The name of the file containing the message prompt.
        
        Returns:
            str: The message prompt.
        """
        file_path = os.path.join(Constants.BASE_FILE_PATH, file_name)
        with open(file_path, 'r') as f:
            return f.read()
