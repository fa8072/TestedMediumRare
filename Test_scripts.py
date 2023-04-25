from tkinter import *
from tkinter import messagebox

def click():
    username = username_entry.get()
    password = password_entry.get()

    messagebox.showinfo('Авторизация успешно выполнена', f'{username}, {password}')

root = Tk()
root.title('Авторизация')
root.geometry('500x300')
root.resizable(False, False)
root['bg'] = 'black'

main_label = Label(root,
                   text='Авторизация',
                   font='Helvetica 20',
                   bg='black',
                   fg='white'
                   )
main_label.pack()

username_label = Label(root,
                       text='Имя пользователя',
                       font='Helvetica 12',
                       bg='black',
                       fg='white',
                       padx=10,
                       pady=8
                       )

username_label.pack()

username_entry = Entry(root,
                       font='Helvetica 10',
                       bg='black',
                       fg='lime'
                       )

username_entry.pack()

password_label = Label(root,
                       text='Имя пароль',
                       font='Helvetica 12',
                       bg='black',
                       fg='white',
                       padx=10,
                       pady=8
                       )

password_label.pack()

password_entry = Entry(root,
                       font='Helvetica 10',
                       bg='black',
                       fg='lime'
                       )

password_entry.pack()

send_btn = Button(root,
                  text='Войти',
                  command=click
                  )

send_btn.pack(padx=10, pady=8)

root.mainloop()
