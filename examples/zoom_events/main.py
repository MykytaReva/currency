import os
import databases

from fastapi import FastAPI, Request, HTTPException
from schema import ZoomEventCreate
from models import zoom_event_table
#TO ENV
ZOOM_WEBHOOK_AUTHORIZATION_TOKEN = os.environ['ZOOM_WEBHOOK_AUTHORIZATION_TOKEN']

app = FastAPI()

# берем параметры БД из переменных окружения
DB_USER = os.environ["POSTGRES_USER"]
DB_PASS = os.environ["POSTGRES_PASSWORD"]
DB_HOST = os.environ["POSTGRES_HOST"]
DB_NAME = os.environ["POSTGRES_DB"]
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()



@app.post("/webhook/zoom-events/")
async def webhook_event(
        zoom_event: ZoomEventCreate,
        request: Request,
):
    if request.headers['authorization'] != ZOOM_WEBHOOK_AUTHORIZATION_TOKEN:
        raise HTTPException(status_code=401, detail="Not authorized")


    query = zoom_event_table.insert().values(zoom_event.dict())
    print(query)
    event_id = await database.execute(query)

    print('Event is -->>', zoom_event.event)
    return {"event_id": event_id}

