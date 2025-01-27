# deepseek-python-demo

A simple Python project demonstrating integration with the DeepSeek API.

# Project startup

Prepare virtualenv
```bash
python -m venv myvenv  
```

Go to virtualevn

On Windows:
```bash
myvenv\Scripts\activate
```

On macOS and Linux:
```bash
source myvenv/bin/activate
```


Install the dependencies
```bash
pip install -r requirements.txt
```


Export local dependencies

```bash
pip freeze > requirements.txt
```


## Setting Up the Environment Variables

1. Create a `.env` file in the root of the project:
   ```bash
   touch .env

2. Add the following variable to the `.env` file:
   ```bash
   DEEPSEEK_API_KEY=your_deepseek_api_key_here

Replace your_deepseek_api_key_here with your actual DeepSeek API key.

Ensure the .env file is loaded by the project.


## Run the application

```bash
uvicorn main:app --reload
```