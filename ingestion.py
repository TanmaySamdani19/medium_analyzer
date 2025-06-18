import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings

load_dotenv()

if __name__ == '__main__':
    print('Ingesting...')
    loader = TextLoader("./mediumblog1.txt")
    document = loader.load()