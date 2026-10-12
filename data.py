import pandas as pd
import os

def process_data(api_data):

    results = api_data.get("results",[])
    if not results :

        print("Not Stock Data found. Please enter a valid stock ticker symbol.")
        return None

    df = pd.DataFrame(results)

    print("COLUMNS: ", df.columns.tolist())

    df = df.rename(columns = {

        "v" : "Volume",
        "vw" : "VWAP",
        "o" : "Open",
        "c" : "Close",
        "h" : "High",
        "l" : "Low",
        "t" : "Date",
        "n" : "Number"
        
    })

    print("After Rename: ", df.columns.tolist())

    if "Date" not in df.columns:

        print("DATE column is missing")
        return None

    df["Date"] = pd.to_datetime(df["Date"] , unit = "ms")

    return df

def save_data (df , filename = "data/stock_data.csv"):

    os.makedirs("data", exist_ok=True)
    df.to_csv(filename , index = False)
    print("--Data Saved Succesfully--")

def load_data (filename = "data/stock_data.csv"):

    try:

        df = pd.read_csv(filename)
        df["Date"] = pd.to_datetime(df["Date"]) 
        return df
    
    except FileNotFoundError:

        print("File not found")
        return None