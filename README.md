# Offline PDF specialized Chatbot using TinyLlama and LlamaIndex, sandbox

This project sets up a local chatbot that can answer questions based on the content of PDF documents. It's a symbolic 
sandbox for a more refined version of it, for example, it now specializes on a certain type of scientific articles.
It runs on terminal and it uses:

- [Ollama](https://ollama.com/) to run a local language model (TinyLlama)
- [LlamaIndex](https://github.com/jerryjliu/llama_index) for document indexing and retrieval
- Hugging Face models for local text embeddings
- Python virtual environment for isolated dependencies

## Features

- Offline, local chatbot
- Processes and understands PDF documents
- No OpenAI API or internet connection required after setup (much safer)
- Lightweight and CPU-friendly (runs on machines without a GPU)

## Requirements

- Python 3.8 or higher
- Linux or macOS (for Ollama compatibility)
- ~1 GB of disk space for the TinyLlama model

## Setup

Run the setup script to prepare the environment, install dependencies, and download the model.

```bash
source setup.sh
SETUP
```

Add PDF files in the manual directory. Any number of them is fine, they will provide the context with which the 
chatbot will operate


## Usage

Populate the 
```bash
manuals
```

directory with .pdf files of your choice. It could be a theme, such as a bibliography of a specific topic.

Then run

```bash
source temp_venv/bin/activate
python chatbot.py
```

Be patient, it will take a while before it starts.
Ignore warnings, errors, loading bars. At a certain point the chatbot will tell you that it's ready. 



## File Structure

```
project_root/
├── setup.sh
├── chatbot.py
├── manuals/
│   ├── doc1.pdf
│   └── ...
├── temp_venv/
└── README.md
```


## Areas of improvement

- The model can be less minimal, more refined, run on GPU
- The file set can be much larger
- It can run locally already, but it could be centralized and accessed via networking from terminals
- With limited resources, the usage could be queued
- There could be a more suitable GUI, even a fastAPI app that runs locally, so that it could be used on any browser





