import requests
import time
# def get_TSX_price(ticker):
#     url = "https://app-money.tmx.com/graphql"

#     # Define the GraphQL query payload
#     payload = {
#         "operationName": "getQuoteForSymbols",
#         "query": (
#             "query getQuoteForSymbols($symbols: [String]) {\n"
#             "  quote: getDelayedQuotesFromQMBySymbols(symbols: $symbols) {\n"
#             "    bid\n"
#             "    ask\n"
#             "    bidsize\n"
#             "    asksize\n"
#             "    vwap\n"
#             "    vwapvolume\n"
#             "    lasttradesize\n"
#             "    lasttradedatetime\n"
#             "    __typename\n"
#             "  }\n"
#             "}"
#         ),
#         # "variables": {"symbols": ["BNS"]}
#         "variables": {"symbols": ticker},
#     }

#     # Define the headers, replicating the browser headers from your API call details.
#     headers = {
#         "accept": "*/*",
#         "content-type": "application/json",
#         "locale": "en",
#         "origin": "https://money.tmx.com",
#         "referer": "https://money.tmx.com/",
#         "user-agent": (
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#             "AppleWebKit/537.36 (KHTML, like Gecko) "
#             "Chrome/135.0.0.0 Safari/537.36"
#         ),
#         "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": '"Windows"',
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#     }

#     # Make the POST request with the payload and headers.
#     response = requests.post(url, json=payload, headers=headers)

#     # Print the status code and response text to verify the result.
#     # print("Status Code:", response.status_code)
#     # print("Response Body:", response.text)
#     res = response.json()
#     # print(f"ask:{res["data"]["quote"][0]["ask"]}  bid:{res["data"]["quote"][0]["bid"]}" )
#     bid_prices = []
#     ask_prices = []

#     for i in range(len(res["data"]["quote"])):
#         price_ask = res["data"]["quote"][i]["ask"]
#         price_bid = res["data"]["quote"][i]["bid"]
#         ask_prices.append(price_ask)
#         bid_prices.append(price_bid)

#     return ask_prices,bid_prices

def get_TSX_price(ticker):
    url = "https://app-money.tmx.com/graphql"

    # Define the GraphQL query payload
    payload = {
    "operationName": "getQuoteBySymbol",
    "query": """query getQuoteBySymbol($symbol: String, $locale: String) {
                  getQuoteBySymbol(symbol: $symbol, locale: $locale) {
                    symbol
                    name
                    price
                  }
                }""",
    "variables": {"symbol": ticker, "locale": "en"}
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
    price = res["data"]["getQuoteBySymbol"]["price"]
    return price

def get_canadian_prices():
    while True:
        print_str = ""
        symbols = ["/GCSPUSD","^COMPX:US","SPXD", "BNS", "QQD", "ZWU", "ARTG", "AGI", "T","GDXU","ABX","K","SPY:US","TSLZ:US"]
        for i in symbols:
            price = get_TSX_price(i)
            print_str += f" {i}:{price}"
        print(print_str)
        time.sleep(5)

get_canadian_prices()


# priceChange
#                     percentChange
#                     exchangeName
#                     exShortName
#                     exchangeCode
#                     marketPlace
#                     sector
#                     industry
#                     volume
#                     openPrice
#                     dayHigh
#                     dayLow
#                     MarketCap
#                     MarketCapAllClasses
#                     peRatio
#                     prevClose
#                     dividendFrequency
#                     dividendYield
#                     dividendAmount
#                     dividendCurrency
#                     beta
#                     eps
#                     exDividendDate
#                     longDescription
#                     fulldescription
#                     website
#                     email
#                     phoneNumber
#                     fullAddress
#                     employees
#                     shareOutStanding
#                     totalDebtToEquity
#                     totalSharesOutStanding
#                     sharesESCROW
#                     vwap
#                     dividendPayDate
#                     weeks52high
#                     weeks52low
#                     alpha
#                     averageVolume10D
#                     averageVolume20D
#                     averageVolume30D
#                     averageVolume50D
#                     priceToBook
#                     priceToCashFlow
#                     returnOnEquity
#                     returnOnAssets
#                     day21MovingAvg
#                     day50MovingAvg
#                     day200MovingAvg
#                     dividend3Years
#                     dividend5Years
#                     datatype
#                     issueType
#                     close
#                     qmdescription
#                     __typename
