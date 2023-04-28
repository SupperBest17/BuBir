from rang import qizil
from crud import pr_add, show_prALL, deleted, update
from menusi import menu


def menuniki():
    while True:
        choice = menu()
        if choice == "1":
            show_prALL()
        elif choice == "2":
            pr_add()
        elif choice == "3":
            deleted()
        elif choice == "4":
            update()
        elif choice == "5":
            break
        else:
            qizil("BUNDAY AMAL MAVJUD EMAS")

menuniki()


