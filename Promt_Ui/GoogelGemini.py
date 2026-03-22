from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()

import streamlit as st

st.header('Reasearch Tool')
# user_input=st.text_input('Enter You promts')
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.7)

paper_input=st.selectbox('Select Reasearch Paper',["Attention all you need ","BERT","Google Gemini"] )

style_input=st.selectbox('Select Explaintion Type',['Begieer-Friendly','Mathmatical','Techincal'])

length_input=st.selectbox('Select Explanination length',['1-2 short para','median 3-4 para','Long para (detail Explanation)'])

template = PromptTemplate(
    template=""" 
please summary the ReaSearch paper titled "{paper_input}" with the following Specification:
Explanation type : {style_input}
Explanation Length : {length_input}

1. Mathematical Details:
    - Include relevant mathematical equation if present in the paper.
    Explain the mathematical concepts using simple, inituation code snippets where
    applicable.
2.Analogies:
    -Use relatable analogies to simplify complex ideas/

If certain information is not available in the paper, respond with: "Insufficent information available" instead of gussing.
Ensure the summary is clear, accurate, and aligned with the provided stytle and length
    
""",
input_variables=['paper_input','style_input','style_input'],
validate_template=True  # Tell all the variable name use in input variales are present over there are not if not it will not work on devploment side
)

promt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input': length_input
})

# result=model.invoke(user_input)

if st.button('Summary'):
    result=model.invoke(promt)
    st.write(result.content)
