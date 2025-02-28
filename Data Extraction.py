import pandas as pd
import pymysql
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)

# Database credentials
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "shivansh"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DATABASE = "bank_loan_crm"

# Function to configure the database connection
def configure_database():
    try:
        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USERNAME,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            port=MYSQL_PORT,
            autocommit=True  
        )
        print(f" Database connected successfully.")
        return connection
    except Exception as e:
        print(f"Database configuration failed: {e}")
        return None  # Return None if connection fails

# Establish connection
connection = configure_database()
if connection:
    cursor_obj = connection.cursor()
    sql_statement = "SELECT * FROM loan_recovery"
    cursor_obj.execute(sql_statement)
    columns = [desc[0] for desc in cursor_obj.description]
    df = pd.DataFrame(cursor_obj.fetchall(), columns=columns)
    print(df)
else:
    print("Dataframe not build")

def store_loan_dataset(df):
    info = logging.basicConfig(level=logging.INFO)
    Warning = logging.basicConfig(level=logging.WARNING)
    folder_path = "D:\ML case studies\components\Dataset\loan_data.csv"
    try:
        file_saving = df.to_csv(folder_path)
        if file_saving:
            return info
        else:
            return Warning
    except Exception as e:
        return e
    
store_loan_dataset(df)
