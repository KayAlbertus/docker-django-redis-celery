from core.models import exchange_modal
import json
import requests 
import os

class PriceUpdate():

    def getPriceFromExchangeSaveToDb():   
        try:
            key = os.environ.get('ALPHAKEY')
            url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey='+key
            print(url)
            r = requests.get(url)
            data = r.json()
            
            array = json.dumps(data)
            a = json.loads(array)
            exchangeRateObj = a["Realtime Currency Exchange Rate"]
            exchangeRate = exchangeRateObj["5. Exchange Rate"]
            lastRefreshed = exchangeRateObj["6. Last Refreshed"]

            collection = exchange_modal.objects.all().count()
            if collection == 0 :
                exchange_object = exchange_modal.objects.create(current_price = exchangeRate,last_refreshed =lastRefreshed )
                exchange_object.save(update_fields=["current_price","last_refreshed"])
            elif collection > 0:
                update_exchange_price = exchange_modal.objects.first()                
                exchange_modal.objects.filter(current_price = update_exchange_price.current_price).update(current_price = exchangeRate,last_refreshed =lastRefreshed)
        
            print(exchangeRateObj)
            print(exchangeRate)

        except Exception as e:
            print("Error!", e.__class__, "occurred.")

        return "New Price Saved"
