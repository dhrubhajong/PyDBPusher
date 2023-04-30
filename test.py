import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="dummy_json",
    user="postgres",
    password="dhrub@123"
)

# Create a cursor object
cur = conn.cursor()

# Define and create the schema
cur.execute("CREATE SCHEMA my_schema")
conn.commit()

# Create the table
cur.execute("CREATE TABLE my_schema.my_table (id SERIAL PRIMARY KEY, name VARCHAR(50))")
conn.commit()

# Insert some data
cur.execute("INSERT INTO my_schema.my_table (name) VALUES ('John'), ('Jane')")
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
