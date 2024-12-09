import psycopg2
import pandas as pd
from config import Config

conn = psycopg2.connect(Config.DATABASE_URI)

df = pd.read_sql_query("SELECT * FROM records", conn)

df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df)
print(df.columns)