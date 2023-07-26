from dotenv import load_dotenv
import os
# from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

loader = TextLoader("./documents.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
question = "Résume moi le document"
data = index.query(question)
print(data)

#llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
"""
from langchain.document_loaders import WebBaseLoader

# Document loader
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
# Index that wraps above steps
index = VectorstoreIndexCreator().from_loaders([loader])
# Question-answering
question = "Qu'est ce que la decomposition de taches ?"
data = index.query(question)
print(data)
"""