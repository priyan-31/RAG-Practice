import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


current_dir = os.path.dirname(os.path.abspath(__file__))    #define the persistent directory
persistent_directory = os.path. join(current_dir, "db", "chroma_db")


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")  ##define the embedding model

db = Chroma(persist_directory=persistent_directory,   
embedding_function=embeddings)                        #load the existing vector store with the embedding function


query = "What is Odyssey?"           #define the user's question

retriever = db.as_retriever(
search_type="similarity_score_threshold",
search_kwargs={"k": 3, "score_threshold": 0.4},)        #retrieve relevant documents based on the query

relevant_docs = retriever.invoke(query)

print("\n --- Relevant Documents --- ")          #display the relevant results with metadata
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown') }\n")