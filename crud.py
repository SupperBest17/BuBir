from sqlite_pCRUD import mahsulotlar, commit, cursor, product_add
from rang import yashil, qizil




@commit
def show_prALL():
    for index, product in enumerate(mahsulotlar, start=1):
        print(f"{index}: {product}")


@commit
def pr_add():
    title = input("Nomi: ")
    company = input("Kompaniyasi: ")
    description = input("Ta'rif: ")
    price = int(input("Narx: "))
    qoshish = (title, company, description, price)
    cursor.execute(product_add, qoshish)
    yashil("Muvoffaqiyatli saqlandi")


@commit
def update():
    show_prALL()
    id = int(input(" ====> "))
    pr = cursor.execute(f"""select * from products where id={id}""").fetchone()
    if not pr:
        print("Noto'g'ri ma'lumot kiritildi")
    else:
        title = input("Nomi: ")
        company = input("Kompaniya: ")
        description = input("Ta'rif: ")
        price = input("Narxi: ")

        cursor.execute(f"""
        update products set title='{title}', company='{company}', description='{description}', price={price}
        """)
        yashil("Muvoffaqiyatli saqlandi")



@commit
def deleted():
    show_prALL()
    id = int(input("ID: "))
    product = cursor.execute(f"""select * from products where id={id}""").fetchone()


    if not product:
        qizil("Xato ma'lumot kiritildi")

    else:
        cursor.execute(f"""
        delete from products where id={id}
        """)
        yashil("Muvoffaqiyatli o'chirildi")
