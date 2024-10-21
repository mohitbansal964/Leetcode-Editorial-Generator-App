# Leetcode Editorial Generator App

## Overview

The Leetcode Editorial Generator Service is a Python-based application designed to generate detailed editorials for Leetcode problems using OpenAI's language model. The service formats the problem details into a chat message template and invokes the language model to produce the editorial content.

## Features

- **Automated Editorial Generation**: Generate detailed editorials for Leetcode problems using OpenAI's language model.
- **Customizable Prompts**: Use custom system and human message prompts to tailor the editorial generation process.
- **Modular Design**: Clean and modular code structure for easy maintenance and extension.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/mohitbansal964/leetcode-editorial-generator.git
    cd leetcode-editorial-generator
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Set Up OpenAI API Key**:
    - Obtain your OpenAI API key from the [OpenAI website](https://beta.openai.com/signup/).
    - Set the API key as an environment variable:
        ```bash
        export OPENAI_API_KEY='your_openai_api_key'  # On Windows use `set OPENAI_API_KEY=your_openai_api_key`
        ```

2. **Prepare Prompt Files**:
    - Ensure you have the following files in the `prompts` directory:
        - `system_message_prompt.txt`: Contains the system message prompt.
        - `human_message_prompt_template.txt`: Contains the human message prompt template.

## Usage

### Example Code
Refer to `main.py` for example code.

## Directory Structure
```
LEETCODE-EDITORIAL-GENERATOR-APP/
├── app/
│   ├── src/
│   │   ├── constants/
│   │   │   ├── __init__.py
│   │   │   └── constants.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── code_info_model.py
│   │   ├── prompts/
│   │   │   ├── human_message_prompt_template.txt
│   │   │   └── system_message_prompt.txt
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── leetcode_editorial_generator_service.py
│   │   └── __init__.py
│   ├── app.py
│   ├── main.py
│   └── __init__.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Further Enhancements
1. **Validation**: Add validation to ensure that the properties in `CodeInfoModel` are set with valid values.
2. **Serialization**: Implement methods to serialize and deserialize the `CodeInfoModel` object to and from JSON.
3. **Configuration Management**: Consider using a configuration file or environment variables for better management of constants and API keys.
4. **Error Handling**: Enhance error handling to manage potential issues such as file not found errors or API call failures.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/mohitbansal964/Leetcode-Editorial-Generator-App/blob/main/LICENSE) file for details.