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
prompt="""ANKIT GHOSH
ag9822@srmist.edu.in   |    6294230462   |    2027
B.Tech, Artificial Intelligence
Address : mullai boys hostel, potheri, tamil nadu, chennai
Summary
Results-oriented Machine Learning / NLP Engineer with strong practical expertise in Natural Language Processing and 
Transformer-based architectures, delivering scalable and production-ready AI systems. Highly proficient in Python, PyTorch, 
NumPy, Pandas, and scikit-learn, with proven end-to-end ownership across data processing, model training, evaluation, 
optimization, and deployment. Deep understanding of Transformers, attention mechanisms, text summarization, and 
embeddings, including hands-on experience fine-tuning and deploying models such as T5. Solid foundation in Data Structures 
& Algorithms (Python and Java) and system-level design for robust ML pipelines. Actively expanding into Computer Vision and 
multimodal learning to build comprehensive AI solutions. Well-prepared to contribute immediately to high-impact engineering 
teams at Microsoft, Amazon, or Google with clean, reliable, and scalable machine learning systems.
Education
SRM IST-Kattankulathur
B.Tech  ·  Artificial Intelligence
H.S.Memorial School
10th  ·  Computer Science  ·  Janai, West Bengal
Swarajya Senior Secondary School
12th  ·  Computer Science  ·  Alwar, Rajasthan
Experience
2027
CGPA - 8.20/10
Mar 2020 - Jun 2021
8.89
Feb 2022 - Jul 2023
7.78
PRS Neurosciences  |  https://prsneurosciences.com/
ML Intern  ·  Intern  ·  Full-Time
Jun 2025 - Present
Virtual
Built an automated image preprocessing pipeline with pose-based subject isolation and background reduction to 
standardize human-centric datasets.
Optimized storage and performance using Guetzli and MozJPEG compression while preserving model-ready image quality.
Designed a modular, scalable workflow supporting single-image and batch processing, improving efficiency for downstream 
computer vision tasks.
Sasken Technologies  |  Link
Softwere Devoloper  ·  Full-Time
Dec 2025 - Present
Sector V, Bidhannagar, Kolkata, within 
the Bengal Intelligent Park
Developed a zero-shot conversational learning framework for a robotic system, enabling real-time knowledge validation 
and incremental learning from human speech input.
Built a multilingual speech understanding and natural language processing pipeline supporting speaker-independent 
recognition, sentence normalization, and intent extraction.
Integrated cloud-based large language model (LLM) inference with on-device memory systems, enabling scalable, 
context-aware, low-latency human–robot interaction.
1 / 3
Projects
Smart Retail Replenishment & Demand Forecasting System (SRR-DFS)  |  
https://github.com/ankitghoshthecreator/Retail_Demand_Forecasting
Individual Project  ·  Python, pandas, numpy, scikit-learn, matplotlib, seaborn, 
Streamlit, Time-series lag features, Moving Average, Safety Stock & Reorder Point 
modeling
Jan 2026 - Jan 2026
Data Science
Developed a SKU-level demand forecasting and inventory optimization system using Python and Random Forest, improving 
replenishment accuracy and reducing stockout risk.
Implemented ABC inventory classification and automated reorder point calculations with safety stock modeling to enhance 
inventory turnover efficiency.
Built an interactive Streamlit dashboard delivering real-time demand forecasts, sell-through analytics, and actionable 
restocking recommendations for retail operations.
Exactly-Once Payment Processing System with Distributed Ledger 
Consistency  |  https://github.com/ankitghoshthecreator/transactionEngine
Individual project  ·  Python, Pytorch, OpenCV, Numpy, Pandas, MediaPipe, Scikit 
Learn
Dec 2025 - Feb 2026
Java Backend Developement
Designed a fault-tolerant financial transaction system ensuring exactly-once money movement across distributed services 
using idempotency, state machines, and ledger-based consistency.
Designed a distributed payment processing architecture to guarantee exactly-once transaction execution under retries, 
failures, and concurrent requests
Implemented a transaction state machine (INIT  AUTHORIZED  SETTLED  FAILED) to enforce deterministic financial 
state transitions
Built an idempotency layer to prevent duplicate debits/credits during network retries and API replays
Document Intelligence Tool   |  Link
·  
FastAPI · React · LangChain · FAISS · sentence-transformers · Gemini Flash · Pyhon
Apr 2026 - Present
Machine Learing, Web Devolopement
Built a production-ready RAG-based document intelligence system aligned with enterprise workflows similar to Zoho Docs, 
WorkDrive, and Sign — engineering the full pipeline from PDF ingestion to grounded Q&A using PyMuPDF, LangChain, 
sentence-transformers (all-MiniLM-L6-v2), and FAISS vector search.
Implemented automated document summarization and structured key clause extraction (payment terms, obligations, 
deadlines) rendered as a JSON-backed table — directly applicable to contract intelligence use cases like Zoho Sign.
Designed a context-aware chat interface with source attribution and chunk-level confidence scoring for answer grounding, 
deployed on Render (backend) and Vercel (frontend) with a modular, production-grade architecture.
UNITY- HandGestureControlledGame  |  Link
·  
Python, Mediapipe, PyTorch, Unity, C#
Feb 2025 - Present
Game
Developed a two-player 2D Unity game integrating hand gesture recognition via MediaPipe and PyTorch-based 
reinforcement learning for adaptive gameplay.
Designed and trained RL agents to learn gesture-response patterns, improving accuracy and player experience over time.
Optimized real-time inference, gesture-to-action mapping, and gameplay performance for smooth and responsive 
multiplayer interaction.
Phaadu - A Math Heavy Programming Language  |  https://github.com/
ankitghoshthecreator/Phaadu
Individual   ·  rust
1. 
Nov 2025 - Present
Programming Language
Built a custom programming language from first principles, using a formally defined grammar and a structured 
tokenization system that handles user-defined symbols and operator hierarchies.
2. 
3. 
4. 
5. 
Implemented a lexer–parser pipeline based on fundamental automata and grammar concepts, converting raw text 
into a validated AST while maintaining predictable parsing behavior.
Developed a deterministic interpreter using well-defined evaluation rules, executing expressions, managing variable 
bindings, and ensuring consistent runtime semantics.
Designed the architecture for extensibility, allowing new syntax constructs, operators, and future compilation targets 
without rewriting core components.
Added robust error diagnostics, using structured position tracking and controlled failure states to generate clear syntax 
and runtime error messages.
2 / 3
Certifications
Programming in Java  |  https://drive.google.com/file/
d/1zhf_9a_gtrkqKoErrqI9Ibk773OAvJfw/view?usp=drivesdk
NPTEL  ·  NPTEL24CS105S252505015
Data Base Management System  |  https://drive.google.com/file/
d/1skKhKAEoL0MXDhNYULJ65bPT-jH1eaUq/view?usp=drivesdk
NPTEL  ·  NPTEL25CS145S533211819
Publications
Nov 2024
Sep 2025
Adaptive Portfolio Optimization using Robbins–Monro Stochastic 
Approximation:.  |  https://zenodo.org/records/17559546
Nov 2025
zenodo
Developed an adaptive portfolio optimization framework using Robbins–Monro stochastic approximation, enabling real
time weight updates under non-stationary market conditions.
Implemented volatility-aware learning via EWMA-based modeling, dynamically tuning risk penalty ( ) 
and learning rate 
( ) to balance return maximization and risk control.
Evaluated model on 10+ years of financial data (Yahoo Finance), achieving robust performance (22.8% annualized 
return, Sharpe ≈ 1.0) with improved stability over static portfolio baselines.  
Skills
Programming Languages: Python, Java, GO, C/C++
Tools and Technologies: OpenCV, Transformers, YOLO, pytorch, Mediapupe, Streamlit 
Areas of Interest: Natural Language Processing
Languages and Frameworks: Spring Boot
Design and Simulation Tools: Unity C#
Domain Knowledge: Speaker Identification 
Languages
English [Professional Working Proficiency], Bengali [Native Proficiency], Hindi [Native Proficiency], Russian [Limited Working 
Proficiency], Chinese [Fundamental Proficiency], Korean [Fundamental Proficiency], Japanese  [Elementary Proficiency]
Links
GitHub, LinkedIn, Instagram, LeetCode, HackerRank, Link
3 / 3"""

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