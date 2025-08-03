import os
from dotenv import find_dotenv, load_dotenv
import streamlit as st
from src.models import CodeInfoModel
from src.services import LeetcodeEditorialGeneratorService

class LeetcodeEditorialGeneratorApp:
    def __init__(self):
        self.__api_key = self.__get_openai_api_key()
        self.__editorial = ""
        self.__has_error = False
        self.__show_preview = False
    
    def __reinit(self):
        self.__editorial = ""
        self.__has_error = False
        self.__show_preview = False
    
    def runner(self):
        """
        Main function to set up the Streamlit app.
        """
        self.__reinit()
        st.set_page_config(page_title="Leetcode Editorial Generator", layout="wide", page_icon="📝")
        st.title("Leetcode Editorial Generator 📝")
        st.caption("using OpenAI's gpt-4.1 model")
        st.warning("Users are advised to review the editorial before publishing.", icon="⚠️")
        col1, col2 = st.columns(2)
        with col1:
            self.__generate_code_info_form()
        with col2:
            self.__display_output()

        self.__display_preview()

    def __initialize_environment(self):
        """
        Loads environment variables from a .env file.
        """
        load_dotenv(find_dotenv(), override=True)

    def __get_openai_api_key(self) -> str:
        """
        Retrieves the OpenAI API key from environment variables.

        Returns:
        -------
        str
            The OpenAI API key.
        """
        self.__initialize_environment()
        api_key = os.environ.get('OPENAI_API_KEY')
        return api_key

    def __leetcode_editorial_generator(self, code_info_model: CodeInfoModel) -> str:
        """
        Generates a Leetcode editorial using the provided code information model.

        Parameters:
        ----------
        code_info_model : CodeInfoModel
            The model containing code information.
        
        Returns:
        -------
        str
            The generated editorial or an error message.
        """
        try:
            llm_chain_service = LeetcodeEditorialGeneratorService(self.__api_key)
            editorial = llm_chain_service.invoke(code_info_model)
            self.__has_error = False
            return editorial
        except Exception as e:
            print(e.with_traceback(e.__traceback__))
            self.__has_error = True
            return ""
        
    def __generate_sidebar_for_api_key(self):
        if 'openai_api_key' in st.session_state:
            self.__api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password", value=st.session_state['openai_api_key'])
        else:
            self.__api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
            st.session_state['openai_api_key'] = self.__api_key

    def __generate_code_info_form(self):
        """
        Generates a form for inputting code information and triggers editorial generation.
        """
        if not self.__api_key:
            self.__generate_sidebar_for_api_key()
        
        with st.form("code_info_form", clear_on_submit=False):
            if not self.__api_key:
                st.info("Please add your OpenAI API key to continue.")
            is_form_disabled = not self.__api_key

            code_info_model = CodeInfoModel(
                problem_heading=st.text_input("🧩 Enter Problem Heading*", disabled=is_form_disabled),
                description=st.text_area("📝 Enter Brief Solution Description", disabled=is_form_disabled),
                lang=st.text_input("⚙️ Enter Solution Language*", disabled=is_form_disabled),
                code=st.text_area("💻 Enter Code*", height=500, disabled=is_form_disabled)
            )
            show_preview = st.checkbox("👁️ Show preview", disabled=is_form_disabled)
            submitted = st.form_submit_button("🚀 Submit", disabled=is_form_disabled)

            if submitted:
                if not code_info_model.problem_heading:
                    st.error("Please add Problem Heading")
                elif not code_info_model.lang:
                    st.error("Please add Language")
                elif not code_info_model.code:
                    st.error("Please add Code")
                else:
                    self.__show_preview = show_preview
                    with st.spinner('Generating...'):
                        self.__editorial = self.__leetcode_editorial_generator(code_info_model)

    def __display_output(self):
        """
        Displays the generated editorial or a prompt to submit the form.
        """
        st.subheader("Output")
        if self.__editorial:
            st.code(self.__editorial, language="markdown")
        elif self.__has_error:
            st.error("Failed to generate editorial. Please try again later.")
        else:
            st.markdown("*Please submit form to generate editorial!*")

    def __display_preview(self):
        """
        Displays a preview of the generated editorial if enabled.
        """
        if self.__show_preview and not self.__has_error:
            with st.container(border= True):
                st.subheader("👁️ Preview")
                st.markdown(self.__editorial)

if __name__ == "__main__":
    app = LeetcodeEditorialGeneratorApp()
    app.runner()
