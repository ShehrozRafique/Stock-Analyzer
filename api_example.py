import requests

api_key = ""

base_url = "https://api.massive.com/v2/aggs/ticker/{symbol}/range/1/day/{from_date}/{to_date}"

def get_stockdata(symbol):

    start_date = "2026-06-06"
    end_date = "2026-10-06"

    url = base_url.format(

        symbol = symbol, 
        from_date = start_date,
        to_date = end_date

    )

    headers = {

        "Authorization" : f"Bearer {api_key}"

    }

    response = requests.get(url, headers=headers)
    return response.json()