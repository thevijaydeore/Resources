from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(); client = OpenAI()

vs_id = "<add your vector store ID>"

def ask(q):
    r = client.responses.create(
        input=q, model="gpt-4o-mini",
        tools=[{"type": "file_search", "vector_store_ids":[vs_id]}]
    )
    return r.output[-1].content[0].text

print(ask("What is IV Therapy?"))