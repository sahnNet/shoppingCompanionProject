import sqlite3

DATABASE_NAME = 'database.db'
USER_TABLE_NAME = "user"
BILL_TABLE_NAME = "bill"
ORDER_TABLE_NAME = "order"


def creat_user_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f''' CREATE TABLE IF NOT EXISTS {USER_TABLE_NAME}
         (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            [User Chat ID] INT NOT NULL
          )
          ''')
    conn.commit()
    conn.close()


def creat_bill_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {BILL_TABLE_NAME}
         (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            [User ID] INT NOT NULL,
            status VARCHAR(50) NOT NULL,
            FOREIGN KEY ([User ID]) REFERENCES user (ID)
          )
          ''')
    conn.commit()
    conn.close()


def creat_order_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS [{ORDER_TABLE_NAME}]
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            [Bill ID] INT NOT NULL,
            Commodity VARCHAR(50) NOT NULL,
            Value VARCHAR(50) NOT NULL,
            FOREIGN KEY ([Bill ID]) REFERENCES bill (ID)
          )
          ''')
    conn.commit()
    conn.close()


def creat_tables():
    creat_user_table()
    creat_bill_table()
    creat_order_table()


def get_user_id(user_chat_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = cursor.execute(f"SELECT ID FROM {USER_TABLE_NAME} WHERE [User Chat ID] = {user_chat_id}")
        conn.commit()
        result = id.fetchone()[0]
    except:
        raise Exception

    conn.close()

    return result


def add_user(user_chat_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = get_user_id(user_chat_id)
        conn.commit()
        result = id.fetchone()[0]
    except:
        cursor.execute(f"INSERT INTO {USER_TABLE_NAME} ([User Chat ID]) VALUES ({user_chat_id})")
        id = get_user_id(user_chat_id)
        conn.commit()
        result = id.fetchone()[0]

    conn.close()

    return result


def get_bill_id(user_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = cursor.execute(f"SELECT ID FROM {BILL_TABLE_NAME} WHERE [User ID] = {user_id} AND status = 'open'")
        conn.commit()
        result = id.fetchone()[0]
    except:
        raise Exception

    conn.close()

    return result


def add_bill(user_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = get_bill_id(user_id)
        conn.commit()
        result = id.fetchone()[0]
    except:
        cursor.execute(f"INSERT INTO {BILL_TABLE_NAME} ([User ID],status) VALUES ({user_id},'open')")
        id = get_bill_id(user_id)
        conn.commit()
        result = id.fetchone()[0]

    conn.close()

    return result


def close_bill(bill_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    result = False
    try:
        cursor.execute(f"UPDATE {BILL_TABLE_NAME} SET status = 'close' WHERE ID = {bill_id}")
        conn.commit()
        result = True
    except:
        pass

    conn.close()

    return result


def get_order_id(bill_id: int, commodity: str, value: str):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = cursor.execute(
            f"SELECT ID FROM {ORDER_TABLE_NAME} WHERE [Bill ID] = {bill_id} AND Commodity = {commodity} AND Value = {value}")
        conn.commit()
        result = id.fetchone()[0]
    except:
        raise Exception

    conn.close()

    return result


def get_orders_by_bill_id(bill_id: int):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    id = cursor.execute(
        f"SELECT Commodity,Value FROM {ORDER_TABLE_NAME} WHERE [Bill ID] = {bill_id}")
    conn.commit()
    result = id.fetchall()

    conn.close()

    return result


def add_order(bill_id: int, commodity: str, value: str):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        id = get_order_id(bill_id, commodity, value)
        conn.commit()
        result = id.fetchone()[0]
    except:
        cursor.execute(
            f"INSERT INTO {ORDER_TABLE_NAME} ([Bill ID],Commodity,Value) VALUES ({bill_id},{commodity},{value})")
        id = get_order_id(bill_id, commodity, value)
        conn.commit()
        result = id.fetchone()[0]

    conn.close()

    return result


# Only when this is the original executable file is the condition true
if __name__ == '__main__':
    creat_tables()
    # print(add_user(158))
