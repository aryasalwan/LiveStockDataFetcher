import yfinance as yf
import time
import requests
import re
import requests
import json
import feedparser

# The API endpoint


def get_TSX_price(ticker):
    url = "https://app-money.tmx.com/graphql"

    # Define the GraphQL query payload
    payload = {
        "operationName": "getQuoteForSymbols",
        "query": (
            "query getQuoteForSymbols($symbols: [String]) {\n"
            "  quote: getDelayedQuotesFromQMBySymbols(symbols: $symbols) {\n"
            "    price\n"
            "    bid\n"
            "    ask\n"
            "    bidsize\n"
            "    asksize\n"
            "    vwap\n"
            "    vwapvolume\n"
            "    lasttradesize\n"
            "    lasttradedatetime\n"
            "    __typename\n"
            "  }\n"
            "}"
        ),
        # "variables": {"symbols": ["BNS"]}
        "variables": {"symbols": ticker},
    }

    # Define the headers, replicating the browser headers from your API call details.
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "locale": "en",
        "origin": "https://money.tmx.com",
        "referer": "https://money.tmx.com/",
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/135.0.0.0 Safari/537.36"
        ),
        "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
    }

    # Make the POST request with the payload and headers.
    response = requests.post(url, json=payload, headers=headers)

    # Print the status code and response text to verify the result.
    # print("Status Code:", response.status_code)
    # print("Response Body:", response.text)
    res = response.json()
    # print(f"ask:{res["data"]["quote"][0]["ask"]}  bid:{res["data"]["quote"][0]["bid"]}" )
    prices = []
    for i in range(len(res["data"]["quote"])):
        price_ask = res["data"]["quote"][i]["price"]
        prices.append(price_ask)
    return prices


def get_canadian_prices():
    while True:
        symbols = ["SPXD", "BNS", "QQD", "ZWU", "ARTG", "AGI", "T"]
        prices = get_TSX_price(symbols)
        print_str = ""
        for i, j in zip(symbols, prices):
            print_str += f" {i}:{j}"

        print(print_str)
        time.sleep(10)


def get_feed(last_title):
    rss_url = "https://feeds.bloomberg.com/markets/news.rss"
    feed = feedparser.parse(rss_url)
    # breakpoint()
    title = feed["entries"][0]["title"]
    # publsihed=(feed["headers"]["date"])
    publsihed = feed["feed"]["updated"]
    try:
        summary = feed["entries"][0]["summary"]
        if last_title != title:
            print(f"Bloomberg\n{title}\n{publsihed}\n{summary}")
            return [title, publsihed, summary]
    except:
        print("No summary")
        return 

import feedparser
def get_feed_gnm(last_title):
    rss_url="https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/investing/"
    feed = feedparser.parse(rss_url)
    # breakpoint()
    title = feed["entries"][0]["title"]
    # publsihed=(feed["headers"]["date"])
    publsihed = feed["feed"]["updated"]
    summary = feed["entries"][0]["summary"]
    if last_title != title:
        print(f"G&M\n{title}\n{publsihed}\n{summary}")
        return [title, publsihed, summary]

last_title = ""
last_title_gnm = ""
before_open=False
while True:
    priceES = round(
        yf.Ticker("ES=F").history(interval="1m", period="1d").iloc[-1]["Close"], 3
    )
    priceG = round(
        yf.Ticker("GC=F").history(interval="1m", period="1d").iloc[-1]["Close"], 3
    )
    if before_open==True:
        print(f"ES=F {priceES}   GC=F {priceG}")
    else:
        priceM = round(
            yf.Ticker("META").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceAMZ = round(
            yf.Ticker("AMZN").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceSPXD = get_TSX_price(["SPXD"])[0]
        priceSPY = round(
            yf.Ticker("%5EGSPC").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        # priceBNS =round(yf.Ticker("BNS.TO").history(interval="1m",period="1d").iloc[-1]["Close"],3)
        priceBNS = get_TSX_price(["BNS"])[0]

        priceGDXU = round(
            yf.Ticker("GDXU.TO").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceARTG = round(
            yf.Ticker("ARTG.V").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceQQD = round(
            yf.Ticker("QQD.TO").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceNSDQ = round(
            yf.Ticker("%5EIXIC").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceTD =round(yf.Ticker("TD.TO").history(interval="1m",period="1d").iloc[-1]["Close"],3)
        pricePLTD = round(
            yf.Ticker("PLTD").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceZWU = round(
            yf.Ticker("ZWU.TO").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceNVDA = round(
            yf.Ticker("NVDA").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceTSLZ = round(
            yf.Ticker("TSLZ").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        pricePLTR = round(
            yf.Ticker("PLTR").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
        priceBTCUSD=round(
            yf.Ticker("BTC-USD").history(interval="1m", period="1d").iloc[-1]["Close"], 3
        )
    
        priceBTCY=get_TSX_price("BTCY")[0]
        # news=yf.Search("tariffs",news_count=1).news
        # breakpoint()
        priceNA = get_TSX_price(["NA"])[0]
        priceTD = get_TSX_price(["TD"])[0]
        priceCM = get_TSX_price(["CM"])[0]
        priceRY = get_TSX_price(["RY"])[0]
        priceBMO = get_TSX_price(["BMO"])[0]
        priceAGI = get_TSX_price(["AGI"])[0]
    #     print(
    #         f"\nES=F {priceES}  SPY:{priceSPY} SPXD: {priceSPXD} TSLZ: {priceTSLZ} GC=F {priceG} META {priceM} \
    # AMZN {priceAMZ} PLTR:{pricePLTR} PLTD: {pricePLTD} BNS: {priceBNS} AGI: {priceAGI}  NSDQ: {priceNSDQ} NVDA: {priceNVDA} \
    # NA:{priceNA} TD:{priceTD} CM:{priceCM} RY:{priceRY} BMO:{priceBMO} BTC:{priceBTCUSD} BTCY:{priceBTCY}"
    #     )
        print(
            f"\nES=F {priceES}  SPY:{priceSPY} SPXD: {priceSPXD} TSLZ: {priceTSLZ} GC=F {priceG} META {priceM} ZWU: {priceZWU} \
    AMZN {priceAMZ} PLTR:{pricePLTR} PLTD: {pricePLTD} BNS: {priceBNS} GDXU: {priceGDXU} ARTG: {priceARTG} AGI: {priceAGI} QQD:{priceQQD} NSDQ: {priceNSDQ} NVDA: {priceNVDA} \
    NA:{priceNA} TD:{priceTD} CM:{priceCM} RY:{priceRY} BMO:{priceBMO} BTC:{priceBTCUSD} BTCY:{priceBTCY}"
        )
    content = get_feed(last_title)
    if content != None:
        last_title = content[0]

    content_gnm = get_feed_gnm(last_title_gnm)
    if content_gnm != None:
        last_title_gnm = content_gnm[0]
    time.sleep(61)


# import requests

# URL of the API
# url = "https://finance.yahoo.com/quote/%5EGSPC/"


# # Headers to mimic a browser and respect specific policies of the server
# headers = {
#     'User-Agent': 'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
#     'Referer': 'https://finance.yahoo.com',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept': 'application/json',
# }

# response = requests.get(url,headers=headers)

# # Print the response text (JSON in this case)
# print(response.text)
