from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name  = "sentence-transformers/all-MiniLM-L6-v2")

result_query_vector = embedding.embed_query("Alaska is the largest state in the USA")

docs = ["The capital of California is Sacramento",
        "The capital of New Jersey is Trenton.",
        "The capital of Illinois is Springfield."]

result_doc_vector = embedding.embed_documents(docs )