# DeepSeek RAG Model

A Retrieval-Augmented Generation (RAG) implementation using DeepSeek's language models.

## Overview

This project implements a RAG system that:

1. Takes a user query
2. Searches the web for relevant information using DuckDuckGo
3. Extracts URLs from the search results
4. Scrapes webpage with Langchain WebBaseLoader -> LangChain helps connect AI to real-world knowledge
5. Embeds scraped document using HuggingFace Embeddings
6. Stores embedding in a FAISS (Facebook AI Similarity Search)
7. Converts FAISS vector into a retriever to fetch documents
8. Constructs QA pipeline that queries retreiver to fetch relevant document chunks
9. Passes retrieved content to the LLM
10. Generates a comprehensive response based on the retrieved context

## Vocabulary

### Embedding

To see an exmample of embedding

```py
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Generate embeddings for text
text = "This is a sample sentence for embedding."
text_embedding = embeddings.embed_query(text)
# The result is a vector (list of numbers)
```

[0.01929548569023609, 0.01642497442662716, 0.07273904979228973, ...]

### FAISS

FAISS is a library developed by Facebook AI Research for efficient similarity search and clustering of dense vectors.
It allows for quick retrieval of vectors that are similar to a query vector.

```py
# Create a FAISS index
index = faiss.IndexFlatL2(dimension)  # L2 distance (Euclidean)
index.add(vectors)  # Add vectors to the index
```

Would output:
> Indices of 5 nearest neighbors: [[381 503  88 359 140]]

### FAISS Vector Store

A FAISS Vector Store integrates FAISS with document storage, allowing you to store document embeddings and retrieve
them efficiently based on similarity.

### Retreiver

A retriever is a component that fetches relevant documents from a data source based on a query. It acts as an interface between the query and the document store.

```py
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load the saved vector store
embeddings = HuggingFaceEmbeddings()
# Setting allow_dangerous_deserialization to True
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)  

# Convert vector store into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Retrieve relevant documents for a query
query = "What is LangChain?"
retrieved_docs = retriever.get_relevant_documents(query)
```

Would output
> Content: LangChain is a framework for developing applications powered by language models.
> Source: docs

### QA Pipeline Querying Retriever

When a QA pipeline queries a retriever, it:
Takes the user's question
Passes it to the retriever to fetch relevant documents
Combines these documents with the question in a prompt for the LLM
Returns the LLM's response based on the retrieved context

## Features

- Web search integration with DuckDuckGo
- Document retrieval and processing
- Vector embeddings using sentence-transformers
- FAISS vector database for efficient similarity search
- DeepSeek Coder 1.3B model for response generation

## Demo

- Question: What is the latest on DeepSeek models?

```
- Helpful Answer: DeepSeek has released several new models, 
including DeepSeek-V3, DeepSeek-R1, and DeepSeek Coder. 
These models are designed to perform better and more 
efficiently than their rivals, and they are all open source. 
They are available for free to use.
```

- Question: Who is Professor En-Hui Yang

```
Extracted Response: Professor En-Hui Yang is a faculty member in the 
Department of Electrical and Computer Engineering at the University 
of Waterloo since June 1997. He is a former Tier 1 Canada Research Chair 
holder in Information Theory and Multimedia Data Compression. He is the 
founding director of the Leitch-University of Waterloo multimedia communications 
lab, a co-founder of SlipStream Data Inc. (now a subsidiary of BlackBerry 
(formerly Research In Motion)), and the founder of BicDroid Inc. He currently 
serves as an Executive Council Member of the China Overseas Friendship 
Association, an Expert Advisor for the Overseas Chinese Affairs Office of the 
State Council of China, a member of IEEE Founders Medal Committee, and an 
advisor for other national and provincial bodies.
```

- Question: Who is Waterloo student Ali Taha

```
Extracted Response: Ali Taha is a 3rd-year Computer Engineering student at 
the University of Waterloo. He does Software Engineering and ML research.
```

^It extracts the above information by going directly to my website!

## How does it get this?

Let us take the example of how it got information about the professor.

```
--------------------------------------------------
Using device: cuda
--------------------------------------------------

--------------------------------------------------
Searching for: Who is Professor En Hui Yang?
--------------------------------------------------

--------------------------------------------------
Search results:
[{'title': 'En-Hui Yang | Electrical and Computer Engineering - University of Waterloo', 
'href': 'https://uwaterloo.ca/electrical-computer-engineering/profile/ehyang'}, 
'href': 'https://uwaterloo.ca/multicom-research-group/research-team/about-director'...]

--------------------------------------------------
URLs extracted:
['https://uwaterloo.ca/electrical-computer-engineering/profile/ehyang', ...]

--------------------------------------------------
Loaded documents:
[Document(metadata={'source': 'https://uwaterloo.ca/electrical-computer-engineering/profile/ehyang'}, page_content="Dr. En-Hui Yang is a Professor ...")]

--------------------------------------------------
Vector store created.
--------------------------------------------------

--------------------------------------------------
QA Chain created.
--------------------------------------------------

--------------------------------------------------
Extracted Answer:
Professor En-Hui Yang is a faculty member in the Department of Electrical and Computer Engineering at the University of Waterloo since June 1997. ...
--------------------------------------------------
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
