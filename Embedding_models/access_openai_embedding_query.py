from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Dimensions : it will indicate how many dimensions we want in the output, when converting from text to vector.
# we can have anything, 200, 300, etc. More dimension we give, it will  capture more context. 
# If we use small vector the cost will be less
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=50)

result = embedding_model.embed_query("Austin is the Capital of Texas.")

print(str(result)) 