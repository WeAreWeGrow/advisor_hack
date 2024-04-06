# from dotenv import load_dotenv, find_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter,RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from io import BytesIO
import openai
import os
from tool.llm import LlmEngine

#API_KEY
def get_openai_key():
    # _ = load_dotenv(find_dotenv())
    return "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"
    return os.environ['OPENAI_API_KEY']


def get_pdf_text(pdf):
  #pdf_reader = PdfReader(pdf)
  #pdf_reader = open(pdf)
  text = pdf.read()
  decoded_text = text.decode('utf-8')
  return decoded_text
  

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""],
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def st_first():
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF 💬")
    with open("C:/Users/thein/Hack-Prototype/pdfs/Tell_us_about_yourself.txt") as file:
       st.download_button(
          label="Tell us about yourself - Download the file for us to know you better",
          data=file
          )

def main():
  st_first()
  # upload file
  pdf = st.file_uploader("Upload the Text file with your responses, please", type="txt")
  openai.api_key = get_openai_key()
  if pdf is not None:
    text = get_pdf_text(pdf)
    chunks = get_text_chunks(text)
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)
        llm = LlmEngine()
        chain = llm.get_qa_chain(knowledge_base)
        with get_openai_callback() as cb:
           response = chain({"query": user_question})
           print(cb)  
        st.write(response['result'])

    

if __name__ == '__main__':
    main()
