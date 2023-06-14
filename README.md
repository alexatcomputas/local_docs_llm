# Testing out LLM for processing / querying local documents
Following guide on [Medium: gpt4all-is-the-local-chatgpt-for-your-documents](https://artificialcorner.com/gpt4all-is-the-local-chatgpt-for-your-documents-and-it-is-free-df1016bc335)
- Original Guide GH repo: [github/fabiomatricardi](https://github.com/fabiomatricardi/GPT4All_Medium)

### Installed and run on Linux:penguin:, should also work on Mac:green_apple:. Windows needs some modifications to compile C binaries, see the original guide for notes.
1. Add pdf documents to the docs folder to use as knowledge base

2. Download models into models directory:
   1. [gpt4all-converted.bin](https://huggingface.co/mrgaang/aira/blob/main/gpt4all-converted.bin)
   2. [Alpacca-7B-ggml](https://huggingface.co/Pi3141/alpaca-native-7B-ggml/tree/397e872bf4c83f4c642317a5bf65ce84a105786e)


1. create and activate venv:
   > python3 -m venv venv<br>
   > source venv/bin/activate
2. Install requirements:
   > (venv) > pip install -r requirements.txt
3. Run db_loading for querying documents:<br>
   > python3 -m db_loading <br>
4. Ask question in interactive terminal