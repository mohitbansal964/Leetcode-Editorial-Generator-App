class Constants:
    """
    A class to encapsulate constant values used throughout the application.
    
    Attributes:
        BASE_FILE_PATH (str): The base directory path where prompt files are stored.
        SYS_MSG_FILE_NAME (str): The file name for the system message prompt.
        HUMAN_MSG_FILE_NAME (str): The file name for the human message prompt template.
    """

    BASE_FILE_PATH: str = "prompts"
    SYS_MSG_FILE_NAME: str = "system_message_prompt.txt"
    HUMAN_MSG_FILE_NAME: str = "human_message_prompt_template.txt"
    GPT_MODEL: str = "gpt-4o"
