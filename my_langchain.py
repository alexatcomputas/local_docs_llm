# Import of langchain Prompt Template and Chain
from langchain import LLMChain, PromptTemplate

# Callbacks manager is required for the response handling
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Import llm to be able to interact with GPT4All directly from langchain
from langchain.llms import GPT4All

local_path = "./models/gpt4all-converted.bin"
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

template = """Question: {question}

Answer: Please summarize and provide a short answer.

"""
prompt = PromptTemplate(template=template, input_variables=["question"])
# initialize the GPT4All instance
llm = GPT4All(model=local_path, callback_manager=callback_manager, verbose=True)
# link the language model with our prompt template
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Hardcoded question
# question = "What Formula 1 pilot won the championship in the year Leonardo di Caprio was born?"

# User imput question...
question = input("Enter your question: ")

# Run the query and get the results
llm_chain.run(question)
