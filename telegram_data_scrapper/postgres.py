import pandas as pd
import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'telegram'
DB_USER = 'postgres'
DB_PASS = 'postgres'

# Load cleaned data
cleaned_data = pd.read_csv('scraped_data/DoctorsET_validated.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
cur = conn.cursor()

# Create table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS doctors_et (
    message_id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    text TEXT NOT NULL
);
'''
cur.execute(create_table_query)
conn.commit()

# Store cleaned data in PostgreSQL
for index, row in cleaned_data.iterrows():
    insert_query = sql.SQL('''
        INSERT INTO doctors_et (message_id, date, text)
        VALUES (%s, %s, %s)
    ''')
    cur.execute(insert_query, (row['message_id'], row['date'], row['text']))

conn.commit()

# Close the connection
cur.close()
conn.close()