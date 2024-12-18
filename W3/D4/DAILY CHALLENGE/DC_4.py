import requests
import random
import psycopg2
from psycopg2 import sql

# Step 1: Fetch all countries
response = requests.get('https://restcountries.com/v3.1/all')
if response.status_code == 200:
    countries = response.json()
    print(f"Successfully fetched {len(countries)} countries.")
else:
    print(f"Failed to fetch countries. Status code: {response.status_code}")
    exit()

# Step 2: Connect to PostgreSQL (make sure the database exists)
DB_HOST = "localhost"
DB_NAME = "DI_SQL_XP"
DB_USER = "postgres"  # Replace with your PostgreSQL username
DB_PASSWORD = "1234"  # Replace with your PostgreSQL password
DB_PORT = '5433'
# Connect to PostgreSQL and create database if necessary

try:
    # First, connect to the default 'postgres' database to create a new database if it doesn't exist
    conn = psycopg2.connect(
        host=DB_HOST,
        database="postgres",  # Default database to connect to initially
        user=DB_USER,
        password=DB_PASSWORD,
        port = DB_PORT
    )
    conn.autocommit = True  # Enable autocommit to allow database creation
    cursor = conn.cursor()
    print("Connected to PostgreSQL.")

    # Check if the database exists, create it if not
    cursor.execute(sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"), [DB_NAME])
    if cursor.fetchone() is None:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")
    conn.close()

    # Now connect to the newly created (or existing) database
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port = DB_PORT
    )
    cursor = conn.cursor()

except Exception as e:
    print(f"Failed to connect to PostgreSQL: {e}")
    exit()

# Create table if not exists
# try:
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS countries (
#             id SERIAL PRIMARY KEY,
#             name TEXT NOT NULL,
#             capital TEXT,
#             flag TEXT,
#             subregion TEXT,
#             population INTEGER
#         )
#     """)
#     print("Table `countries` created or verified successfully.")
# except Exception as e:
#     print(f"Error creating table: {e}")
#     conn.close()
#     exit()

# Step 3: Randomly select 10 countries
random_countries = random.sample(countries, 10)
print(f"Randomly selected {len(random_countries)} countries.")
# print(type(random_countries))

# Step 4: Extract relevant data
def extract_country_data(country):
    for i in range(10):
        name = country[i]['name']['common']
        capital = country[i]["capital"][0] if "capital" in country and country["capital"] else None
        flag = country[i]["flags"]["png"]
        subregion = country[i]["subregion"]
        population = country[i]["population"]

        query = '''
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.execute(query, (name, capital, flag, subregion, population))

        conn.commit()
        print("Data has been committed to the database.")
    conn.close()
    print("Connection closed.")

extract_country_data(random_countries)
