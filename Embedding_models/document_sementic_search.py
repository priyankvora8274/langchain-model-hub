from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

def sementic_search(documents, query):
    doc_vector = embedding_model.embed_documents(documents)
    query_vector = embedding_model.embed_query(query)
    
    similarity_scores = cosine_similarity([query_vector],doc_vector)
    
    #Option 1:  high_index, high_score = (sorted(list(enumerate(similarity_scores[0])),key=lambda x:x[1])[-1])

    #Option 2: 
    high_index = np.argmax(similarity_scores[0])
    high_score = similarity_scores[0][high_index]

        
    
    print(query)
    print(documents[high_index])
    print(f"Similarity score : {high_score}")

documents = [
    "Texas is famous for its cowboy culture, barbecue, and large cities like Houston and Dallas.",
    "California is known for Hollywood, beautiful beaches, and Silicon Valley.",
    "Florida is popular for its sunny weather, theme parks, and beautiful beaches.",
    "New York is famous for New York City, the Statue of Liberty, and Times Square.",
    "Arizona is known for the Grand Canyon, desert landscapes, and hot summers."
]
query = "Tell me about Florida!"

sementic_search(documents,query)