from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

loader = TextLoader("./documents.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
question = "Résume moi le document"
index.query(question)