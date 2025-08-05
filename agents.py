# agents.py
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import google.generativeai as genai
from crewai import Agent, Task , LLM
load_dotenv()  # This loads the .env file
 
from crewai import Agent, Task
 
os.getenv("GOOGLE_API_KEY")
 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
 
llm_model= LLM(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini/gemini-1.5-flash",
)
 
#llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
#llm = genai.GenerativeModel(model=llm_model, temperature=0.7)
 
tweet_summarizer = Agent(
    role='Technical Summary Analyst',
    goal='Summarize the latest 5 tweets concisely',
    backstory='You are an expert at summarizing social media content.',
    verbose=True,
    allow_delegation=False,
    llm=llm_model
)
 
content_suggester = Agent(
    role='Content Strategy Expert',
    goal='Suggest high-engagement tweet ideas based on recent posts',
    backstory='You specialize in social media growth and engagement tactics.',
    verbose=True,
    allow_delegation=False,
    llm=llm_model
)
 
def get_tasks(tweet_data: str):
    summary_task = Task(
        description=f"Summarize the following tweets:\n\n{tweet_data}",
        expected_output="A concise summary of the 5 tweets",
        agent=tweet_summarizer
    )
 
    suggestion_task = Task(
        description=f"Based on these recent tweets:\n\n{tweet_data}\n\nSuggest a new tweet idea that will boost engagement.",
        expected_output="One or two tweet ideas optimized for engagement.",
        agent=content_suggester
    )
 
    return [summary_task, suggestion_task]