# My Generative AI and Text-to-Speech Project

This project uses Google's Generative AI  gemini 1.5 and convert Google Text-to-Speech to generate text responses and convert them into speech.

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create `api_key_secret.py`**:
    - Create a file named `api_key_secret.py` in the project directory and add your API key:
    ```python
    # api_key_secret.py
    API_KEY = "Your_API_Key_Here"
    from this https://aistudio.google.com/app/apikey or search google ai studio you can get your api key from here
    also read document it official documentation with code detail

    i have used  api_key_secret.py and imported its content in main file for hiding api key dont expose your api key to other 
    ```

3. **Install Dependencies**:
    - Make sure you have the required libraries installed:
    ```sh
    pip install google-generativeai  gtts
    gtts convert text into audio you can find detail about modules from pypi
    ```

4. **Run the Script**:
    - Execute the main script:
    ```sh
    python main.py
    ```

## Usage

- The script will prompt you to enter a prompt, generate a response using AI, convert it to speech, and play the audio.

## Contributing

- Feel free to fork the repository and submit pull requests.

## License

- This project is licensed under the MIT License.

