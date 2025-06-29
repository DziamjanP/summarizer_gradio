# Summary maker

Simple project on gradio with use of LLM's to produce text's summary. Supports pdf parsing with OCR.

# Setup

To setup you will need to install all python dependencies:
```
pip install -r requirements.txt
```

OCR for pdf parsing requires tesseract, for debian systems it can be installed with:
```
apt install tesseract-ocr
```
To start the app with gradio interface you'll need to launch `main.py`:
```
python main.py
```
`.env` contains API keys to together.ai and mistral.ai

# How it works

Text is fed into LLM using mistral.ai or together.ai API. Prompts used are stored in `prompt.txt` and `prompt_long.txt` for longer texts, when text is processed in chunks.

## PDF

PDF is parsed in `parser.py`. It combines raw text and parses data from tables and images (using pytesseract for OCR).

## Extra long texts

Text is checked to fit into the length limits (around 6k characters, with 2k reserved for prompts), if it overshoots next operations are performed:
- Text is split into batches by 6k in the nearest new line or space character, if none are present it hard splits on 6k
- First batch is fed into the model to get it's summary
- Next batch is fed along with previous summary. Prompt asks model to update this summary with new data from the new batch
- Loop repeats until all data is processed

## Model selection

Default model is Magistral Medium, it showed good perfomance on tests
However model selection is available. All listed models were tested and results are showed in the next section.

### Available models

These models were tested through human evaluation and came out with results:

- Llama-3.3-70B-Instruct-Turbo-Free (together.ai)
  - Lower latency
  - Worse prompt following
  - Can produce too long unstructured summaries
- DeepSeek-R1-Distill-Llama-70B-free (together.ai)
  - Higher latency
  - Needs careful prompt adjusting, still barely follows them
  - Good summary quality with right prompt and a bit of luck
- magistral-medium (mistral api)
  - Is a reasoning model
  - Best summary quality relative to other models
  - Good prompt following
- mistral-medium (mistral api)
  - Similar to magistral medium
  - Worse summary quality
  - Worse prompt understanding

LLM benchmarks like livebench and model usage prices (only free ones were used) were taken into account. The final choice was magimistral-medium.

# Examples
Examples of a summary are in the `examples` directory.
`N.txt` contains text or links and `N.md` contains summaries.