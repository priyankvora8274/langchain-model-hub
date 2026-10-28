from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temprature: It is indicating the randoness in the output of the model .We can define how cretive our output we want.
# let say if we are doing any creative task like storywriting, poem, thn we should choose 1.5+ temprature.

# max_completion_tokens: Will define what max amount token should be used in output, we can here consider token as words.
# the usage of token only decides billing, so for usecase where we want to resrict the use of token we can define this limit.
model = ChatOpenAI(model = 'gpt-5.2', temperature=0.1, max_completion_tokens=10)

result = model.invoke("Who is Presidet os USA?")

print(result.content)