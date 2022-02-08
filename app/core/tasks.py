
from celery import shared_task
from app import settings
from core.price_update import PriceUpdate

#Celery Task To Update Price
@shared_task(bind=True)
def get_price_feed(self):
    PriceUpdate.getPriceFromExchangeSaveToDb()
    return "Done"