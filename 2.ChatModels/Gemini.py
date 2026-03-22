
from langchain_google_genai import ChatGoogleGenerativeAI


from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.5)


result = model.invoke("I want to die , IS this sentence is negative or postive")

print(result.content)