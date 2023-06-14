# Testing out LLM for processing / querying local documents
Following guide on [Medium: gpt4all-is-the-local-chatgpt-for-your-documents](https://artificialcorner.com/gpt4all-is-the-local-chatgpt-for-your-documents-and-it-is-free-df1016bc335)
- Original Guide GH repo: [github/fabiomatricardi](https://github.com/fabiomatricardi/GPT4All_Medium)

## The files here are all installed and run on Linux, should also work on Mac. Windows needs some modifications to compile C binaries, see the original guide for notes.
1. Add pdf documents to the docs folder to use as basis for query knowledge base

2. Download models into models directory: (They are quite large and are therefore gitignored)
   1. [gpt4all-converted.bin](https://huggingface.co/mrgaang/aira/blob/main/gpt4all-converted.bin)
   2. [Alpacca-7B-ggml](https://huggingface.co/Pi3141/alpaca-native-7B-ggml/tree/397e872bf4c83f4c642317a5bf65ce84a105786e)

- Had to pip install llama-cpp-python upon first run of > python3 my_knowledge_qna.py

# Run db_loading for querying documents
3. python3 -m db_loading