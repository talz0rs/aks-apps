from celery import Celery
from database import SessionLocal
from models import Item


celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)


@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def process_item(item_id):
    db = SessionLocal()
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item is None:
            return f"item {item_id} no found"
        item.status = "processed"
        db.commit()
        return f"item {item_id} processed"
    finally:
        db.close()
