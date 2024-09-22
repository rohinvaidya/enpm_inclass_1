import requests
import pandas as pd

def loading_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    data = response.json()
    df = pd.DataFrame(data)
    return df