from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage


model = ChatMistralAI(
    model_name="mistral-small-latest",
    temperature=0.9
)

messages = [
    SystemMessage(content="You are a web developer")
]
print("-----------Welcome to the WEB Developer Chat bot---------------")
print("Type 0 to exit")
while True:
    prompt = input("You : ")
    if(prompt == "0"):
        break
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    print(response.content)
    messages.append(AIMessage(content=response.content))


print(messages)