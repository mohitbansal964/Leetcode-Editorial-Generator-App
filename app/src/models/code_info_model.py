from dataclasses import dataclass

@dataclass
class CodeInfoModel:
    """
    A data class to encapsulate information about a coding problem, including its heading, description, 
    programming language, and the code itself.
    """
    problem_heading: str = ""
    description: str = ""
    lang: str = ""
    code: str = ""