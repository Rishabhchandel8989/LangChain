from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
    # temperature=0.7,
    # max_new_tokens=128,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is capital of Uttar Pradesh?")
print(result.content)
