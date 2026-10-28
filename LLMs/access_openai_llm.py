#notes: LLMs are no longer being used much nowadays, so it is not recommended to use this.
# It will be deprecated

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

result = openai_llm.invoke("What is the name of president of the USA?")

print(result)
