from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history=[
    SystemMessage(content='How can i help you today') # doing because it help the llm to understand the meta data each time we are sending
]


while True:               # This chat bot it will run infinite time till use type exit
    user_input=input("You: ")

    chat_history.append(HumanMessage(content=user_input)) # converting user input into HumanMessage

    if user_input=='exit':
        break
    ans=model.invoke(chat_history)

    chat_history.append(AIMessage(content=ans.content)) # To AIMessage 
    # st.write(ans.content)
    print("AI: ",ans.content)

print(chat_history)