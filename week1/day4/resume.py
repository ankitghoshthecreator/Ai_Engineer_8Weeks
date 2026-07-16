import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api=os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("api error")
client= Groq(api_key=my_api)
model="llama-3.3-70b-versatile"
role="user"
resumePath="C:\\Users\\Ankit\\ai_engineer_8weeks\\week1\\day4\\ANKIT GHOSH_Doc.pdf"
from langchain_community.document_loaders import PyMuPDFLoader

pyL= PyMuPDFLoader(resumePath)

docs=pyL.load()

print(type(docs))
print(len(docs))
print(type(docs[0]))
print(docs[0])
prompt = "\n".join(doc.page_content for doc in docs)
message={
    "role":role,
    "content":prompt
}
from pydantic import BaseModel
class Res(BaseModel):
    nme:str
    email:str
    phone_num:str
    match:int
schema=Res.model_json_schema()
response_format={
    "type":"json_object"
}

system_prompt=f"""Extract the personal info of the student if the match according the job description is more than 70% strictly follow this schema {schema}
the job description is python, pytorch, open cv, nlp, c++ wrapper"""
message_system={
    "role": "system",
    "content": system_prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)