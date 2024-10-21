import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from src.models import CodeInfoModel
from src.constants import Constants
from langchain_core.output_parsers import StrOutputParser

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
        # Initialize the language model with the specified GPT model and API key
        self.__llm = ChatOpenAI(
            model=Constants.GPT_MODEL,
            api_key=openai_api_key
        )
        # Initialize a string output parser
        self.__parser = StrOutputParser()
    
    def invoke(self, code_info: CodeInfoModel) -> str:
        """
        Invokes the language model with the provided code information and returns the output.
        
        Args:
            code_info (CodeInfoModel): The code information model containing details for the editorial.
        
        Returns:
            str: The content of the language model's response.
        """
        # Create a language model chain using a chat prompt template, the language model, and the parser
        llm_chain = self.__create_chat_prompt_template() \
                    | self.__llm \
                    | self.__parser
        # Invoke the chain with the code information dictionary and return the response
        return llm_chain.invoke(code_info.__dict__)
    
    def __create_chat_prompt_template(self) -> ChatPromptTemplate:
        """
        Creates a chat prompt template using system and human messages.
        
        Returns:
            ChatPromptTemplate: The created chat prompt template.
        """
        # Construct a chat prompt template from system and human messages
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
        # Read the system message content from a file and return a SystemMessage object
        return SystemMessage(content=self.__read_message_prompt(Constants.SYS_MSG_FILE_NAME))

    def __get_human_message_template(self) -> HumanMessagePromptTemplate:
        """
        Retrieves the human message template for the chat prompt.
        
        Returns:
            HumanMessagePromptTemplate: The human message template object.
        """
        # Read the human message template content from a file and return a HumanMessagePromptTemplate object
        return HumanMessagePromptTemplate.from_template(self.__read_message_prompt(Constants.HUMAN_MSG_FILE_NAME))

    def __read_message_prompt(self, file_name: str) -> str:
        """
        Reads and returns the message prompt from a file.
        
        Args:
            file_name (str): The name of the file containing the message prompt.
        
        Returns:
            str: The message prompt.
        """
        # Construct the file path and read the message prompt from the file
        file_path = os.path.join(Constants.BASE_FILE_PATH, file_name)
        with open(file_path, 'r') as f:
            return f.read()
