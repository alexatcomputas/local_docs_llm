import datetime
import os  # for interaaction with the files

from langchain import LLMChain, PromptTemplate
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# to be able to load the pdf files
# function for loading only TXT files
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader, UnstructuredPDFLoader

# LLamaCpp embeddings from the Alpaca model
# from langchain.embeddings import LlamaCppEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings

# Vector Store Index to create our database about our knowledge
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import GPT4All

# text splitter for create chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

# FAISS  library for similaarity search
from langchain.vectorstores.faiss import FAISS

# assign the path for the 2 models GPT4All and Alpaca for the embeddings
gpt4all_path = "./models/gpt4all-converted.bin"
## REMOVED ## llama_path = './models/ggml-model-q4_0.bin'
# Calback manager for handling the calls with  the model
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

## REMOVED ## embeddings = LlamaCppEmbeddings(model_path=llama_path)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# create the GPT4All llm object
llm = GPT4All(model=gpt4all_path, callback_manager=callback_manager, verbose=True)


# Split text
def split_chunks(sources):
    chunks = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=256, chunk_overlap=32)
    for chunk in splitter.split_documents(sources):
        chunks.append(chunk)
    return chunks


def create_index(chunks):
    texts = [doc.page_content for doc in chunks]
    metadatas = [doc.metadata for doc in chunks]

    search_index = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    return search_index


# DEV TESTING
os.environ["PYDEVD_WARN_EVALUATION_TIMEOUT"] = "10"
# /DEV TESTING


def similarity_search(query, index):
    # k is the number of similarity searched that matches the query
    # default is 4
    matched_docs = index.similarity_search(query, k=3)
    sources = []
    for doc in matched_docs:
        sources.append(
            {
                "page_content": doc.page_content,
                "metadata": doc.metadata,
            }
        )

    return matched_docs, sources


# Load our local index vector db
index = FAISS.load_local("my_faiss_index", embeddings)

# create the prompt template
template = """
Please use the following context to answer questions.
Context: {context}
---
Question: {question}
Answer: Let's think step by step."""

# Hardcoded question
# question = "What is a PLC and what is the difference with a PC"
# User-input question: comment the line above and uncomment the following line
question = input("Your question: ")
matched_docs, sources = similarity_search(question, index)
# Creating the context
context = "\n".join([doc.page_content for doc in matched_docs])
# instantiating the prompt template and the GPT4All chain
prompt = PromptTemplate(template=template, input_variables=["context", "question"]).partial(context=context)
llm_chain = LLMChain(prompt=prompt, llm=llm)
# Print the result
print(llm_chain.run(question))
