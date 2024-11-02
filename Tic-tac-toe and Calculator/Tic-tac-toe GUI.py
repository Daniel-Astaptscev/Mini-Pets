from tkinter import *
from tkinter.messagebox import showerror, showinfo


def window_game(player_1, player_2):
    window_g = Tk()
    window_g.title('Tic-Tac-Toe')
    window_g.geometry("406x456+700+200")
    window_g.configure(background='#DDDDDD')
    window_g.resizable(False, False)

    counter = 1

    def notice(symbol):
        if symbol == 'X':
            showinfo(title='Конец игры', message=f'Победил игрок {player_1}! Примите наши искренние поздравления!')
        else:
            showinfo(title='Конец игры', message=f'Победил игрок {player_2}! Примите наши искренние поздравления!')
        window_g.destroy()
        window_start()

    def winner(counter, matrix):
        if len(matrix) >= 5:
            if matrix.get(0, 0) == matrix.get(3, 3) == matrix.get(6, 6):
                notice(matrix.get(0))
            elif matrix.get(1, 1) == matrix.get(4, 4) == matrix.get(7, 7):
                notice(matrix.get(1))
            elif matrix.get(2, 2) == matrix.get(5, 5) == matrix.get(8, 8):
                notice(matrix.get(2))
            elif matrix.get(6, 6) == matrix.get(7, 7) == matrix.get(8, 8):
                notice(matrix.get(6))
            elif matrix.get(0, 0) == matrix.get(1, 1) == matrix.get(2, 2):
                notice(matrix.get(0))
            elif matrix.get(3, 3) == matrix.get(5, 5) == matrix.get(4, 4):
                notice(matrix.get(3))
            elif matrix.get(0, 0) == matrix.get(4, 4) == matrix.get(8, 8):
                notice(matrix.get(0))
            elif matrix.get(6, 6) == matrix.get(4, 4) == matrix.get(2, 2):
                notice(matrix.get(6))
            elif counter == 10:
                showinfo(title='Ничья', message='Никто из игроков не смог победить, объявлена ничья!')
                window_g.destroy()
                window_start()

    def choose(button, number):
        nonlocal counter, matrix
        if counter % 2 != 0 and button['text'] == '':
            button.config(text='X', font=('Bookman Old Style', 24), background='#50AF7B')
            counter += 1
            label_turn.config(text=f'Ход игрока {player_2}, выберите клетку:')
            matrix[number] = button['text']
            winner(counter, matrix)
        elif counter % 2 == 0 and button['text'] == '':
            button.config(text='O', font=('Bookman Old Style', 24), background='#CF6430')
            counter += 1
            label_turn.config(text=f'Ход игрока {player_1}, выберите клетку:')
            matrix[number] = button['text']
            winner(counter, matrix)

    def Lines():
        canvas = Canvas(bg='#DDDDDD', highlightthickness=0)  # highlightthickness=0 убирает рамку вокруг элемента
        canvas.create_line(354, 100, 20, 100, width=3)
        canvas.create_line(354, 200, 20, 200, width=3)
        canvas.create_line(130, 298, 130, 3, width=3)
        canvas.create_line(243, 298, 243, 3, width=3)
        canvas.place(x=15, y=80, width=406, height=400)

    Lines()

    button_1 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_1, 0))
    button_4 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_4, 3))
    button_7 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_7, 6))
    button_2 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_2, 1))
    button_5 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_5, 4))
    button_8 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_8, 7))
    button_3 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_3, 2))
    button_6 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_6, 5))
    button_9 = Button(window_g, background='#DDDDDD', command=lambda: choose(button_9, 8))

    label_turn = Label(window_g, text=f'Ход игрока {player_1}, выберите клетку:',
                       font=('Bookman Old Style', 12, 'bold'),
                       background='#DDDDDD')

    label_turn.place(width=406, height=60)

    button_1.place(x=35, y=83, width=108, height=95)
    button_4.place(x=35, y=183, width=108, height=95)
    button_7.place(x=35, y=283, width=108, height=95)

    button_2.place(x=148, y=83, width=108, height=95)
    button_5.place(x=148, y=183, width=108, height=95)
    button_8.place(x=148, y=283, width=108, height=95)

    button_3.place(x=261, y=83, width=108, height=95)
    button_6.place(x=261, y=183, width=108, height=95)
    button_9.place(x=261, y=283, width=108, height=95)

    matrix = dict()

    window_g.mainloop()


def window_start():
    window_s = Tk()
    window_s.title('Tic-Tac-Toe')
    window_s.configure(background='#DDDDDD')
    window_s.geometry("406x206+700+300")
    window_s.resizable(False, False)

    def button_submit():
        if entry_name_1.get() and entry_name_2.get():
            player_1 = entry_name_1.get()
            player_2 = entry_name_2.get()
            window_s.destroy()
            window_game(player_1, player_2)
        else:
            showerror(title='Ошибка', message='Заполните все поля с именами игроков')

    label_name_1 = Label(window_s, text='Введите имя \n первого игрока:', font=('Bookman Old Style', 14, 'bold'),
                         background='#DDDDDD')
    label_name_1.grid(row=0, column=0, padx=10, pady=10)
    label_name_2 = Label(window_s, text='Введите имя \n второго игрока:', font=('Bookman Old Style', 14, 'bold'),
                         background='#DDDDDD')
    label_name_2.grid(row=0, column=1, padx=10, pady=10)

    entry_name_1 = Entry(window_s, width=17, font=('Bookman Old Style', 12), borderwidth=6)
    entry_name_1.grid(row=1, column=0, padx=10, pady=10)
    entry_name_2 = Entry(window_s, width=17, font=('Bookman Old Style', 12), borderwidth=6)
    entry_name_2.grid(row=1, column=1, padx=10, pady=10)

    button_submit = Button(window_s, text='Начать игру', font=('Bookman Old Style', 14), background='#CCDDFF',
                           command=button_submit)
    button_submit.grid(row=2, columnspan=3, padx=50, pady=20)

    window_s.mainloop()


window_start()
