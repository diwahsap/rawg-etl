import pandas as pd
import mysql.connector
import os

# Define the MySQL database connection parameters
host = 'localhost'
user = 'root'
password = 'dimas123.'
database = 'rawg_db'

# Connect to MySQL and create the database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Create the database if it doesn't exist
create_db_query = f"CREATE DATABASE IF NOT EXISTS {database}"
cursor.execute(create_db_query)

# Close the cursor and connection to create a new connection to the specific database
cursor.close()
conn.close()

# Connect to the specific database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute queries
cursor = conn.cursor()

# Read the CSV file into a DataFrame
# Get the absolute path to the user's home directory
home_dir = os.path.expanduser("~")

# Define the relative path to the CSV file
relative_path = "datasets.csv"  # Replace "datasets.csv" with the actual name of your CSV file

# Combine the home directory with the relative path to get the actual path to the CSV file
csv_file = os.path.join(home_dir, relative_path)

df = pd.read_csv(csv_file)

# Define the table name in the MySQL database
table_name = 'raw_table'  # Replace 'your_table_name' with the desired table name

# Create the table in the MySQL database
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    slug VARCHAR(255),
    name VARCHAR(255),
    playtime INT,
    platforms TEXT,
    stores TEXT,
    released DATE,
    tba BOOLEAN,
    rating FLOAT,
    rating_top INT,
    ratings TEXT,
    ratings_count INT,
    reviews_text_count INT,
    metacritic TEXT,
    tags TEXT,
    esrb_rating TEXT,
    reviews_count INT,
    genres TEXT
)
"""
cursor.execute(create_table_query)

# Insert the data from the DataFrame into the MySQL table
insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({', '.join(['%s'] * len(df.columns))})"
cursor.executemany(insert_query, df.values.tolist())

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
