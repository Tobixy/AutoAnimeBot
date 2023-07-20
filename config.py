from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("28374181"))
API_HASH = getenv("00b7ca7f535e816590db39e76f85d0c7")
BOT_TOKEN = getenv("6370339719:AAGbNkpNu9yMg2npGm13htripTcLw2idK08")

MONGO_DB_URI = getenv("mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001762803339"))
UPLOADS_ID = int(getenv("-1001948604900"))

STATUS_ID = int(getenv("12087"))
SCHEDULE_ID = int(getenv("12090"))

CHANNEL_TITLE = getenv("auto_testhub")
INDEX_USERNAME = getenv("auto_testhub")
UPLOADS_USERNAME = getenv("auto_testhub")
