class CodeInfoModel:
    def __init__(self):
        self.__problem_heading: str = ""
        self.__description: str = ""
        self.__lang: str = ""
        self.__code: str = ""

    @property
    def problem_heading(self) -> str:
        return self.__problem_heading
    
    @problem_heading.setter
    def problem_heading(self, val: str) -> None:
        self.__problem_heading = val

    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, val: str) -> None:
        self.__description = val

    @property
    def lang(self) -> str:
        return self.__lang
    
    @lang.setter
    def lang(self, val: str) -> None:
        self.__lang = val

    @property
    def code(self) -> str:
        return self.__code
    
    @code.setter
    def code(self, val: str) -> None:
        self.__code = val