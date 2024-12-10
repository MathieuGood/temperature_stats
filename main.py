import psycopg2
import pandas as pd
from config import Config
import matplotlib


def get_temp_df() -> pd.DataFrame:
    conn = psycopg2.connect(Config.DATABASE_URI)

    df = pd.read_sql_query(
        "SELECT timestamp, name, temperature, humidity FROM records INNER JOIN devices ON devices.id = records.device_id ",
        conn,
    )
    df = df[df["name"].isin(["Chambre A&M", "Chambre Lucas", "Extérieur", "Salon"])]
    return df

df = get_temp_df()
