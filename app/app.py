import streamlit as st

from src.models import CodeInfoModel
from src.services import LeetcodeEditorialGeneratorService

st.set_page_config(page_title="Leetcode Editorial Generator", layout="wide")
st.title("Leetcode Editorial Generator")
st.caption("using OpenAI's gpt-4o")
st.warning("Users are advised to review the editorial before publishing.",icon="⚠️")
if 'openai_api_key' in st.session_state:
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password", value=st.session_state['openai_api_key'])
else:
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    st.session_state['openai_api_key'] = openai_api_key

editorial = ""
error_in_editorial_generation = False
show_preview = False

def leetcode_editorial_generator(code_info_model: CodeInfoModel):
    global editorial, error_in_editorial_generation
    # Instantiate LLM model
    llm_chain_service = LeetcodeEditorialGeneratorService(openai_api_key)
    # Prompt
    messages = llm_chain_service.format_chat_message(code_info_model)
    try:
        # Run LLM model
        editorial = llm_chain_service.invoke(messages)
        error_in_editorial_generation = False
    except:
        error_in_editorial_generation = True

def generate_code_info_form():
    global show_preview
    with st.form("code_info_form", clear_on_submit = False):
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
        is_form_disabled = not openai_api_key

        code_info_model = CodeInfoModel()
        code_info_model.problem_heading = st.text_input("Enter Problem Heading*", disabled=is_form_disabled)
        code_info_model.description = st.text_area("Enter Brief Solution Description", disabled=is_form_disabled)
        code_info_model.lang = st.text_input("Enter Solution Language*",disabled=is_form_disabled)
        code_info_model.code = st.text_area("Enter Code*", height=500, disabled=is_form_disabled) 
        show_preview_temp = st.checkbox("Show preview",disabled=is_form_disabled)

        submitted = st.form_submit_button("Submit", disabled=is_form_disabled)
        if submitted:
                if not code_info_model.problem_heading:
                    st.error("Please add Problem Heading")
                elif not code_info_model.lang:
                    st.error("Please add Language")
                elif not code_info_model.code:
                    st.error("Please add Code")
                else:
                    show_preview = show_preview_temp
                    with st.spinner('Generating...'):
                        leetcode_editorial_generator(code_info_model)

col1, col2 = st.columns(2)
with col1:
    generate_code_info_form()
with col2:
    st.subheader("Output")
    if editorial:
        st.code(editorial, language="markdown")
    elif error_in_editorial_generation:
        st.error("Failed to generate editorial. Please check your OpenAI API key.")
    else:
        st.markdown("*Please submit form to generate editorial!*")

if show_preview and not error_in_editorial_generation:
    with st.container(border= True):
        st.subheader("Preview")
        st.markdown(editorial)
