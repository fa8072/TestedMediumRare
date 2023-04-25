import tkinter as tk
from SQL.Database_file import connection

app = tk.Tk()

app.title("Best Deal Telephonics")
app.geometry("{}x{}".format(app.winfo_screenwidth(), app.winfo_screenheight()))
app.attributes("-fullscreen", True)
app.minsize(width=600, height=600)


def add_product():
    pass

def del_product(product):
    def _del_product():
        pass

    return del_product


def success_login(user):
    window = tk.Toplevel(app)
    window.title("Товары")

    if user[6] == "admin":
        title_label = tk.Label(window,
                               text="Название")
        title_label.pack()

        title = tk.Entry(window)
        title.pack()

        price_label = tk.Label(window,
                               text="Цена")
        price_label.pack()

        price = tk.Entry(window)
        price.pack()

        add_product_btn = tk.Button(window,
                                    text="Добавить",
                                    command=add_product)

        add_product_btn.pack()



    with connection.cursor() as cursor:
        products = cursor.execute("SELECT * FROM products").fetchall()
    for product in products:
        product_label = tk.Label(window,
                               text= product[1])
        product_label.pack()

        product_label = tk.Label(window,
                               text="-------")
        product_label.pack()
        if user[6] == "admin":
            del_product_btn = tk.Button(window,
                                        text="Удалить",
                                        command=del_product(product))

            del_product_btn.pack()



def click_btn_sign_in():
    window = tk.Toplevel(app)
    window.title("Вход")
    username_label = tk.Label(window,
                              text="Имя пользователя")
    username_label.pack()

    username = tk.Entry(window)
    username.pack()

    password_label = tk.Label(window,
                              text="Пароль")
    password_label.pack()

    password = tk.Entry(window)
    password.pack()

    def sign_in():
        with connection.cursor() as cursor:
            user = cursor.execute("SELECT * FROM users WHERE login = %s", [username.get()]).fetchall()

        if len(user) < 1 or user[0][5] != password.get():
            tk.Label(window, text="Пользователя нет").pack()
            return

        window.destroy()
        window.update()
        success_login(user[0])

    sign_in_btn = tk.Button(window,
                            text="Вход",
                            bg="#eee8aa",
                            fg="#000080",
                            font="Helvetica 20",
                            state="normal",
                            command=sign_in)

    sign_in_btn.pack()


def click_btn_sign_up():
    pass


# Пусть пользователя встречает надпись:

entry_label = tk.Label(text="Здравствуйте! \n Войдите или зарегистрируйтесь для работы с приложением.",
                       bg="#eee8aa",
                       fg="#000080",
                       font="Helvetica 20",
                       height=5,
                       width=100,
                       justify="center"
                       )

entry_label.pack()

# Затем будет две кнопки: вход и регистрация

button_signIn = tk.Button(text="Вход",
                          bg="#eee8aa",
                          fg="#000080",
                          font="Helvetica 20",
                          # Связь с функцией нажатия через command
                          state="normal",  # Состояние кнопки по умолчанию
                          command=click_btn_sign_in
                          )

button_signIn.pack()

button_signUp = tk.Button(text="Регистрация",
                          bg="#eee8aa",
                          fg="#000080",
                          font="Helvetica 20",
                          # Связь с функцией нажатия через command
                          state="normal"  # Состояние кнопки по умолчанию
                          )

button_signUp.pack()

app.mainloop()
