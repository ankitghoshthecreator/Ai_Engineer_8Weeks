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

from pydantic import BaseModel
class Tickit(BaseModel):
    name:str
    phn:str
    email:str
schema=Tickit.model_json_schema()
response_format={
    "type":"json_object"
}
system_prompt=f"""Extrack the personal info stricty based on this schema and give a json output{schema}"""
message_system={
    "role":"system",
    "content":system_prompt
}


text="hey i am ankit, my mobile num is 9685743296 ankitghosh@gmail.com is my mail id"

prompt=f"""this is a customer detail. extract the personal info of{text}"""


message={
    "role":"user",
    "content":prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)


# now load json and use them 

import json
rawJson=answer

data=json.loads(rawJson)
tickit=Tickit(**data)
print(tickit.name)
