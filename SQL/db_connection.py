## Database connection 

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus
load_dotenv(r"C:\Users\mohda\OneDrive\Desktop\Olist Project\SQL\.env")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

print("DB_USER =", DB_USER)
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)
print("DB_NAME =", DB_NAME)
print("DB_PASSWORD =", DB_PASSWORD)
print("DATABASE_URL =", DATABASE_URL)