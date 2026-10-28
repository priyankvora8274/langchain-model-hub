from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

# Here also we will have temperature and max_completion_tokens args
model = ChatAnthropic(model = 'claude-opus-5-5')

result = model.invoke("Who is president of the USA?")

print(result)