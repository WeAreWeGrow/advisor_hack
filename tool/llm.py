from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os


class LlmEngine:

    def __init__(
            self,
            model_name: str = "gpt-3.5-turbo",
            streaming: bool = False
    ):
        self.model_name = model_name
        self.streaming = streaming
        self.openai = ChatOpenAI(
            model_name=self.model_name,
            streaming=self.streaming,
            callbacks=[StreamingStdOutCallbackHandler()],
            openai_api_key=os.getenv("OPENAI_API_KEY"))

    def get_qa_chain(
            self,
            vector_store
    ):
        prompt_template = """Based on the following known content, answer the user's question concisely and professionally.
                                                {context}
                                                Question:
                                                {question}"""

        prompt = PromptTemplate(template=prompt_template,
                                input_variables=["context", "question"])

        return RetrievalQA.from_llm(llm=self.openai,
                                    retriever=vector_store.as_retriever(),
                                    prompt=prompt)
    def get_history_chain(
            self,
            vector_store
    ):
        prompt_template = """Based on the following known content, answer the user's question concisely and professionally.
                                                Known content:
                                                {context}
                                                Question:
                                                {question}"""

        prompt = PromptTemplate(template=prompt_template,
                                input_variables=["context", "question"])

        return ConversationalRetrievalChain.from_llm(llm=self.openai,
                                                     retriever=vector_store.as_retriever(),
                                                     combine_docs_chain_kwargs={'prompt': prompt})