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
prompt="Do you know AI?"

message={
    "role":role,
    "content":prompt
}

messages=[message]

response=client.chat.completions.create(model=model, messages=messages)
print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)