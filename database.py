import sqlite3

DATABASE_NAME = 'database.db'
USER_TABLE_NAME = "user"
BILL_TABLE_NAME = "bill"
ORDER_TABLE_NAME = "order"
USER_BILL_TABLE_NAME = "user_bill"
BILL_ORDER_TABLE_NAME = "bill_order"


def creat_user_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f''' CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME}
         (
            ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            UserID VARCHAR(50) NOT NULL
          )
          ''')
    conn.commit()
    conn.close()


def creat_bill_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {BILL_TABLE_NAME}
         (
            ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY
          )
          ''')
    conn.commit()
    conn.close()


def creat_order_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {ORDER_TABLE_NAME}
         (
            ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            Commodity VARCHAR(50) NOT NULL,
            Value VARCHAR(50) NOT NULL
          )
          ''')
    conn.commit()
    conn.close()


def creat_user_bill_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {USER_BILL_TABLE_NAME}
         (  
            ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            [User ID] INT NOT NULL,
            [Bill ID] INT NOT NULL,
            FOREIGN KEY ([User ID]) REFERENCES user (ID),
            FOREIGN KEY ([Bill ID]) REFERENCES bill (ID)
          )
          ''')
    conn.commit()
    conn.close()


def creat_bill_order_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {BILL_ORDER_TABLE_NAME}
         (
            ID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
            [Bill ID] INT NOT NULL,
            [Order ID] INT NOT NULL,
            FOREIGN KEY ([Bill ID]) REFERENCES bill (ID),
            FOREIGN KEY ([Order ID]) REFERENCES "order" (ID)
          )
          ''')
    conn.commit()
    conn.close()


def creat_tables():
    creat_user_table()
    creat_bill_table()
    creat_order_table()
    creat_user_bill_table()
    creat_bill_order_table()


def add_user(user_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {USER_TABLE_NAME} IF NOT EXISTS  VALUES (:UserID)",
                   {'UserID': user_id})
    conn.commit()
    conn.close()


# Only when this is the original executable file is the condition true
if __name__ == '__main__':
    creat_tables()

# def creat_user(username, password):
#     build_database()
#     conn = sqlite3.connect(DATABASE_NAME)
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"INSERT INTO {TABLE_NAME} VALUES (:user_name,:password)",
#                        {'user_name': username, 'password': password})
#         conn.commit()
#         conn.close()
#         return is_exist(username=username, password=password)
#     except:
#         return None
#
#
# def is_exist(username, password):
#     build_database()
#     conn = sqlite3.connect(DATABASE_NAME)
#     cursor = conn.cursor()
#     try:
#         cursor.execute(f"SELECT rowid,* FROM {TABLE_NAME} WHERE user_name = '{username}' AND password = '{password}'")
#         user = cursor.fetchone()
#
#         conn.commit()
#         conn.close()
#
#         return user[0]
#     except:
#         return None
