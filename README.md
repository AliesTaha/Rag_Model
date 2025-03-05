# DeepSeek RAG Model

A Retrieval-Augmented Generation (RAG) implementation using DeepSeek's language models.

## Overview

This project implements a RAG system that:

1. Takes a user query
2. Searches the web for relevant information using DuckDuckGo
3. Processes the retrieved content using DeepSeek Coder (1.3B instruct model)
4. Generates a comprehensive response based on the retrieved context

## Features

- Web search integration with DuckDuckGo
- Document retrieval and processing
- Vector embeddings using sentence-transformers
- FAISS vector database for efficient similarity search
- DeepSeek Coder 1.3B model for response generation

## Demo

Asking DeepSeek about DeepSeek

```
- Question: What is the latest on DeepSeek models?
- Helpful Answer: DeepSeek has released several new models, including DeepSeek-V3, DeepSeek-R1, and DeepSeek Coder. These models are designed to perform better and more efficiently than their rivals, and they 
are all open source. They are available for free to use.
```

## Requirements

- Python 3.8+
- LangChain
- Transformers
- PyTorch
- FAISS
- DuckDuckGo Search
- Sentence Transformers
- Hugging Face Hub

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/deepseek-rag.git
   cd deepseek-rag
   ```

2. Create a virtual environment (recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Open the `rag.py` file and modify the query variable to ask your own question:

   ```python
   # Change this to your own query
   query = "What is the latest on DeepSeek models?"
   ```

2. Run the script:

   ```
   python rag.py
   ```

3. The script will:
   - Search the web for information related to your query
   - Process the retrieved documents
   - Generate a response using the DeepSeek Coder model
   - Print the extracted response and the full context

## Customization

- To use a different model, change the `model_name` variable in `rag.py`
- Adjust the number of search results by modifying the `max_results` parameter in the `search_and_scrape` function
- Change the embedding model by updating the `model_name` in the `create_retriever` function
