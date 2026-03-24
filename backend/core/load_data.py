import pandas as pd
from core.models import Customer, Product

def load_data():
    df = pd.read_csv("data/customers.csv")

    for _, row in df.iterrows():
        Customer.objects.create(name=row["name"])

from core.load_data import load_data
load_data()