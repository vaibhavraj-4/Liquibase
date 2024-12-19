import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': 'MOHANraj',
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
        print("Database 'my_database' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def create_table(cursor):
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_database.my_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        )
        """)
        print("Table 'my_table' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
        exit(1)

def insert_data(cursor):
    try:
        insert_query = "INSERT INTO my_database.my_table (name, age) VALUES (%s, %s)"
        data = [
            ('Alice', 30),
            ('Bob', 25),
            ('Charlie', 35)
        ]
        cursor.executemany(insert_query, data)
        print(f"Inserted {cursor.rowcount} rows into 'my_table'.")
    except mysql.connector.Error as err:
        print(f"Failed inserting data: {err}")
        exit(1)

def main():
    try:
        # Establish a connection to MySQL
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Create database and table, then insert data
        create_database(cursor)
        create_table(cursor)
        insert_data(cursor)

        # Commit the transaction
        cnx.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

    finally:
        cursor.close()
        cnx.close()

if __name__ == '__main__':
    main()
