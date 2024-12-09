import main as db
import pandas as pd

df = db.df

df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df)
print(df.columns)

df = df.groupby('name', as_index=False).agg(
    {
        'temperature': 'mean',
        'humidity': 'mean',
        'timestamp': 'max'
    }
)
print(df)