import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(query):
    prompt = f"""
    You are a strict SQL generator.

    Database schema:
    core_customer(id, name)
    core_order(id, customer_id)

    IMPORTANT RULES:
    - Use ONLY these table names
    - DO NOT use 'orders' or 'customers'
    - ONLY use 'core_order' and 'core_customer'
    - Return ONLY SQL (no explanation)

    Examples:
    Q: show all orders
    A: SELECT * FROM core_order;

    Q: list all customers
    A: SELECT * FROM core_customer;

    Now convert:
    {query}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()