import requests
import time
from datetime import datetime

BITCOIN_API_URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/kgzBSMAJWPNbf1uwM0nwc0Nyn8rCxNBKrXKVK6pGrKk'

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = response.json()

    #Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

def post_ifttt_webhook(event, value):
    #  The payload that will be sent to IFTTT service
    data = {'value1':value}
    #  Inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    #Sent a HTTP POST request to the webhool url
    requests.post(ifttt_event_url, json=data)

BITCOIN_PRICE_THRESHOLD = 10000

def main():
    bitcoin_history = []
    while(True):
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date':date,'price':price})

        #  Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency',price)

        #  Send a telegram notification
        #  Once we have 5 items in our bitcoin_history sends an update
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_emergency',format_bitcoin_history(bitcoin_history))

            #  Reset thr bitcoin_history
            bitcoin_history = []

        # Sleep for 5 minutes
        time.sleep(5 * 60)

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        #  Formats the date into a string : '15.05.19 15:09'
        date = bitcoin_price['date'].strftime("%d.%m.%Y %H:%M")
        price = bitcoin_price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

        # Use a <br> (break) tag to create a new line
        # Join the rows delimited by <br> tag: row1<br>row2<br>row3
        return '<br>'.join(rows)


if __name__ == '__main__':
    main()
