import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

APIKey = os.getenv("API_KEY")
Model = os.getenv("MODEL")
BaseURL = os.getenv("BASE_URL")

client = genai.Client(api_key=APIKey)
uploaded_file = client.files.upload(file=input("Enter the path to your document. \n"))
    
print(f'Uploaded document name is {uploaded_file.file_name}')

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[uploaded_file, 'Tell me about this document'],
    config={
        'temperature': 0,
        'top_p': 0.95,
        'top_k': 20,
    },
)
print(response.text)