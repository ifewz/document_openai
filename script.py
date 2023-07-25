from dotenv import load_dotenv
import os
from langchain.llms import openai
from langchain.document_loaders import TextLoader

load_dotenv("secrets.env")

llm = openai(openai_api_key=os.getenv("OPENAI_API_KEY"))

loader = TextLoader("./documents.txt")
loader.load()

