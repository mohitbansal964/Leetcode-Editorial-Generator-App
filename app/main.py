import os
from dotenv import load_dotenv, find_dotenv

from src.models import CodeInfoModel
from src.services import LeetcodeEditorialGeneratorService

# loading the API Keys from .env
load_dotenv(find_dotenv(), override=True)

code = """

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        order = []
        def helper(root):
            if root is None:
                return
            for node in root.children:
                helper(node)
            order.append(root.val)
        helper(root)
        return order
"""
if __name__ == "__main__":
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    llm_chain_service = LeetcodeEditorialGeneratorService(openai_api_key)
    code_info_model = CodeInfoModel()
    code_info_model.problem_heading = "590. N-ary Tree Postorder Traversal"
    code_info_model.description = "Postorder Traversal using recursion"
    code_info_model.lang = "Python3"
    code_info_model.code = code
    messages = llm_chain_service.format_chat_message(code_info_model)
    print(llm_chain_service.invoke(messages))