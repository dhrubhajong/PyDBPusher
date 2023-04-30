import psycopg2
import json
from config import config
from log import logging



# Create a global connection variable
conn=None

def create_schema():
    try:
        params = config()
        logging.info("Creating a Schema")
        global conn  # Use the global connection variable
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("CREATE SCHEMA IF NOT EXISTS private")

        conn.commit()
        print("Schema created successfully")
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('database connection terminated. ')

def create_table():
    try:
        global conn  # Use the global connection variable
        cur = conn.cursor()

        create_script = '''
            CREATE TABLE IF NOT EXISTS private.Swiggy (
                id_no VARCHAR(100),
                outlets VARCHAR(200),
                city VARCHAR(100),
                rating TEXT,
                rating_count VARCHAR(200),
                cost_column VARCHAR (200),
                cuisine VARCHAR (300),
                lic_no VARCHAR (300),
                source_link TEXT,
                address TEXT,
                menu TEXT 
            );
        '''

        cur.execute(create_script)

        conn.commit()
        print("Table created successfully")
        logging.info("Created successfull Table")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('database connection terminated. ')

def insert_data(file_path):
    try:
        global conn  # Use the global connection variable
        cur = conn.cursor()

        # Open the JSON file
        with open(file_path) as f:
            data = json.load(f)

        # Iterate over the data and insert each row into the database
        for row in data:
            cur.execute("INSERT INTO private.Swiggy (id_no, outlets, city, rating, rating_count, cost_column, cuisine, lic_no, source_link, address, menu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (row['id_no'],row['outlets'], row['city'], row['rating'],row['rating_count'],row['cost_column'],
                     row['cuisine'],row['lic_no'],row['source_link'],row['address'],row['menu']))

        conn.commit()
        print("Data inserted successfully")
        logging.info("Data inserted successfully on Table")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    #         print('database connection terminated. ')

if __name__ == "__main__":
    create_schema()
    print("Schema created successfully...")
    create_table()
    print("Table created successfully...")
    insert_data(r"C:\Users\lenovo\Downloads\analytical\swiggy.json")
    print("Data inserted successfully...")
    

