class CodeInfoModel:
    """
    A model class to encapsulate information about a coding problem, including its heading, description, 
    programming language, and the code itself.
    """

    def __init__(self):
        """
        Initializes a new instance of the CodeInfoModel class with default values.
        """
        self.__problem_heading: str = ""
        self.__description: str = ""
        self.__lang: str = ""
        self.__code: str = ""

    @property
    def problem_heading(self) -> str:
        """
        Gets the heading of the coding problem.
        
        Returns:
            str: The heading of the coding problem.
        """
        return self.__problem_heading
    
    @problem_heading.setter
    def problem_heading(self, val: str) -> None:
        """
        Sets the heading of the coding problem.
        
        Args:
            val (str): The heading of the coding problem.
        """
        self.__problem_heading = val

    @property
    def description(self) -> str:
        """
        Gets the description of the coding problem.
        
        Returns:
            str: The description of the coding problem.
        """
        return self.__description
    
    @description.setter
    def description(self, val: str) -> None:
        """
        Sets the description of the coding problem.
        
        Args:
            val (str): The description of the coding problem.
        """
        self.__description = val

    @property
    def lang(self) -> str:
        """
        Gets the programming language of the coding problem.
        
        Returns:
            str: The programming language of the coding problem.
        """
        return self.__lang
    
    @lang.setter
    def lang(self, val: str) -> None:
        """
        Sets the programming language of the coding problem.
        
        Args:
            val (str): The programming language of the coding problem.
        """
        self.__lang = val

    @property
    def code(self) -> str:
        """
        Gets the code of the coding problem.
        
        Returns:
            str: The code of the coding problem.
        """
        return self.__code
    
    @code.setter
    def code(self, val: str) -> None:
        """
        Sets the code of the coding problem.
        
        Args:
            val (str): The code of the coding problem.
        """
        self.__code = val
