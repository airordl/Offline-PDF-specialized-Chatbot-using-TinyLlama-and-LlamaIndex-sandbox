#!/bin/bash
SETUP () {

mkdir manuals
python3 -m pip install --upgrade virtualenv
virtualenv temp_venv
temp_venv
source temp_venv/bin/activate
#pip install --upgrade pip
pip install \
  llama-index \
  llama-index-llms-ollama \
  llama-index-embeddings-huggingface \
  llama-index-readers-file \
  sentence-transformers \
  transformers \
  accelerate \
  pymupdf
pip install llama-index-llms-ollama


#if ! command -v ollama &> /dev/null; then
curl -fsSL https://ollama.com/install.sh | sh

ollama pull tinyllama

echo "activate the virtual environment with:"
echo "   source temp_venv/bin/activate"
echo "(ignore all warnings)"
echo "add your PDF files to the 'manuals/' folder."
echo "run the chatbot script with:"
echo "   python chatbot.py"
}
