# ChatGPT Wrapper

A simple web application that provides a custom interface for interacting with OpenAI's ChatGPT API.

## Features
- Clean, modern UI
- Conversation history
- Multiple model selection (GPT-3.5, GPT-4)
- Secure API key storage

## Setup

1. Clone the repository
2. Install dependencies:
```bash
   pip install flask openai
```
3. Add your OpenAI API key in `app.py`
4. Run the application:
```bash
   python app.py
```
5. Open your browser to `http://localhost:3000`

## Security Note
Never commit your actual API key to the repository. Use environment variables in production.

## License
MIT