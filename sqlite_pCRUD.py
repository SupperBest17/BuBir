import sqlite3


connection = sqlite3.connect("products.db")
cursor = connection.cursor()


cursor.execute("""
    create table if not exists products(
        id integer primary key ,
        title varchar (10),
        company varchar ,
        description varchar,
        price integer
    );
""")


product_add = """
        insert into products (title,company, description, price) values (?, ?, ?,?)
    """


mahsulotlar = cursor.execute("""
        select * from products
    """).fetchall()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        connection.commit()
        return result
    return wrapper





