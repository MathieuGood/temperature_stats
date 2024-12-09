import psycopg2
import pandas as pd
from config import Config
import matplotlib

conn = psycopg2.connect(Config.DATABASE_URI)

df = pd.read_sql_query(
    "SELECT timestamp, temperature, humidity, name FROM records INNER JOIN devices ON devices.id = records.device_id ",
    conn,
)
