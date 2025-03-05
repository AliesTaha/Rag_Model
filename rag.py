from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
# load the model bro
model_name = "deepseek-ai/deepseek-coder-1.3B-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map={"": device})

llm_pipeline = pipeline("text-generation", model=model,
                        tokenizer=tokenizer, max_new_tokens=512)
llm = HuggingFacePipeline(pipeline=llm_pipeline)
# search it up


def search_and_scrape(query):
    from duckduckgo_search import DDGS
    from langchain.document_loaders import WebBaseLoader

    results = DDGS().text(query, max_results=2)  # top 2 bros
    urls = [res['href'] for res in results]

    loader = WebBaseLoader(urls)
    return loader.load()  # list of documents
# retrieve the document from bro


def create_retriever(docs):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embedding_model)
    return vectorstore.as_retriever()
# rag pipeline


def rag_query(query):
    docs = search_and_scrape(query)
    retriever = create_retriever(docs)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, retriever=retriever, chain_type="stuff")
    return qa_chain.run(query)


# give question to bro
query = "What is the latest on DeepSeek models?"
response = rag_query(query)
# Extract the part after "helpful answer:"
keyword = "Helpful Answer:"
if keyword in response:
    # Split at the first occurrence and take the second part
    result = response.split(keyword, 1)[1]
    print("\nExtracted Response:", result.strip())
else:
    print("\nKeyword not found in the response.")

print("\nThe context it sees:", response)
