import requests
import datetime
from claude import Claude
import yfinance as yf
from datetime import datetime, timedelta
cookie = "activitySessionId=078d511b-0039-4b55-b924-b0aec31d690a; __cf_bm=HMcZ2uU8q7auZdrQNwwDw3EGVf06bCNICkNxzqUYmlg-1700061331-0-AZWuvME4ABbT4OLC7WHwxsVAzee8eW8fdAxM4PcZdo2OGOWTI+xp3Tsb0URT6nfQHnCkh/h+inzZWPPeKuS+8NE=; cf_clearance=XA.NCt7Yb.waDlrPR5LIXzYTg0f5GEYjtqeSBuDDxUg-1700061332-0-1-a66291c1.39f66ab9.f163ce21-0.2.1700061332; __ssid=6c221d36f9c304801ddbbd676b4ddd6; sessionKey=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; intercom-device-id-lupk8zyo=8da16667-b191-401a-840c-100d7438957d; intercom-session-lupk8zyo=bDdRVUtNbGNmR0NvT21OOXMvWENtWEpCZzdRU1YvdzdsMVZoQkxJSG1nckdNTTY4a0pSL2dVcmd2bTFHeWlxeS0tMjV3dk1JQ2x3MHhXUitRK0R2bzJYZz09--df33b8d6ad8b67de739f01ab30461e0373ed7051"
claude = Claude(cookie)
stock_ticker = str(input("Please enter stock ticker of choice"))

print(f"Company: {stock_ticker}")
prompt = "Research the company that uses the ticker" + str(stock_ticker) + ",Retrieve the initial public offering (IPO) date for the company associated with the ticker symbol " + str(
    stock_ticker) + "Summarize the data in the one short sentence"
prompt2 = "Research the company that uses the ticker" + \
    str(stock_ticker) + ",Retrieve the market capitalization for the company associated with the ticker symbol " + \
    str(stock_ticker) + "Summarize the data in the one short sentence"

response = claude.get_answer(prompt)
# claude.create_new_conversation()
response2 = claude.get_answer(prompt2)


def get_stock_percentage_change(ticker):
    try:
        today = datetime.today().strftime('%Y-%m-%d')

        stock_data = yf.download(ticker, start=today, end=today)

        close_price_today = stock_data['Close'].iloc[-1]
        open_price_today = stock_data['Open'].iloc[0]
        percentage_change = (
            (close_price_today - open_price_today) / open_price_today) * 100

        return percentage_change

    except Exception as e:
        return f"Error: (FUCK) {e}"


percentage_change = get_stock_percentage_change(stock_ticker)
print(f"Percentage Change for {stock_ticker} today: {percentage_change:.2f}%")
print(" ****** ")
print(response)
print(" ****** ")
print(response2)
print(" ****** ")
