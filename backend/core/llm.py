from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

def generate_sql(query):
    prompt = f"""
    You are a SQL generator.

    Tables:
    customers(id, name)
    orders(id, customer_id)
    invoices(id, order_id)
    payments(id, invoice_id)

    Convert this to SQL:
    {query}
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content