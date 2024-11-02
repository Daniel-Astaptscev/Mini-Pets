from tkinter import *
from tkinter import ttk
from BlockA import BlockA
from BlockB import BlockB 
from BlockC import BlockC 
from BlockD import BlockD 
from BlockE import BlockE 
from BlockF import BlockF 
from BlockG import BlockG 
from BlockH import BlockH 


class StartPage():
    def __init__(self, notebook, position_question, position_answer):
        self.frame_1 = ttk.Frame(notebook)
        self.frame_1.pack(fill=BOTH, expand=True)
        notebook.add(self.frame_1, text="Главная")
        self.right_counter = 0

        self.Ticket_1 = BlockA(notebook, position_question, position_answer)
        self.Ticket_2 = BlockB(notebook, position_question, position_answer)
        self.Ticket_3 = BlockC(notebook, position_question, position_answer)
        self.Ticket_4 = BlockD(notebook, position_question, position_answer)
        self.Ticket_5 = BlockE(notebook, position_question, position_answer)
        self.Ticket_6 = BlockF(notebook, position_question, position_answer)
        self.Ticket_7 = BlockG(notebook, position_question, position_answer)
        self.Ticket_8 = BlockH(notebook, position_question, position_answer)

        label_welcome = ttk.Label(self.frame_1, text="Добро пожаловать на экзамен!", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#68779c", foreground="#FFFFFF", padding=8).pack(fill="x")
        
        label_person = ttk.Label(self.frame_1, text=f"Имя и Фамилия экзаменуемого:", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#5c9682", foreground="#FFFFFF", padding=4)
        label_person.pack(fill="x", ipady=60)

        self.entry_person = ttk.Entry(self.frame_1, font=("Times New Roman", 14), width=40)
        self.entry_person.place(x=210, y=140)

        def disabled_entry():
            self.entry_person.configure(state='disabled')
        
        btn_disabled = ttk.Button(self.frame_1, text="Подтвердить", command=disabled_entry)
        btn_disabled.place(x=580, y=140)

        label_border_1 = ttk.Label(self.frame_1, background="#5c9682", foreground="#FFFFFF").pack(fill="x", ipady=20)
        label_border_2 = ttk.Label(self.frame_1, background="#68779c", foreground="#FFFFFF").pack(fill="x", ipady=60)

        btn_end_exam = ttk.Button(self.frame_1, text="Закончить экзамен", command=self.check_all) 
        btn_end_exam.place(x=370, y=310)

        self.label_statistics = ttk.Label(self.frame_1, text=f"Статистика прохождения экзамена:", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#CD5C5C", foreground="#FFFFFF", padding=4)
        self.label_statistics.pack(fill="x", ipady=25)

        self.label_test = ttk.Label(self.frame_1, text=f"В ДАННЫЙ МОМЕНТ ТЕСТ НЕ ПРОЙДЕН", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#CD5C5C", foreground="#FFFFFF", padding=4)
        self.label_test.pack(fill="x", ipady=250)

    def finish_the_exam(self): 
        self.label_test.destroy()
        self.label_statistics.config(background="#5c9682")

        label_percent = ttk.Label(self.frame_1, text=f"Общая сдача экзамена: {round((self.right_counter * 100) / 44)}%", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#5c9682", foreground="#FFFFFF", padding=4)
        label_percent.pack(fill="x", ipady=20)

        label_counter_right = ttk.Label(self.frame_1, text=f"Правильных ответов: {self.right_counter}", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#5c9682", foreground="#FFFFFF", padding=4)
        label_counter_right.pack(fill="x")

        label_counter_wrong = ttk.Label(self.frame_1, text=f"Неправильных ответов: {44 - self.right_counter}", anchor=CENTER, font=("Times New Roman", 14, "bold"), background="#5c9682", foreground="#FFFFFF", padding=4)
        label_counter_wrong.pack(fill="x", ipady=20)

        label_border_3 = ttk.Label(self.frame_1, background="#5c9682", foreground="#FFFFFF").pack(fill="x", ipady=120)

    def check_all(self): 
        window = Toplevel()
        window.title("Проверка доступа")
        window.geometry("310x200")

        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        window_width = width + 2 * frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        window_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - window_width // 2
        y = window.winfo_screenheight() // 2 - window_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()

        label_text = ttk.Label(window, text="Для получения доступа к функции проверки экзамена, введите пароль администратора:", font=("Times New Roman", 14), wraplength=280, justify='center').pack(padx=20, pady=(25, 10))
        label_check = ttk.Entry(window, font=("Times New Roman", 12), justify='center', show='⚠', width=30)
        label_check.pack() 

        def check_access():

            if label_check.get() == 'samrek':
                self.right_counter += self.Ticket_1.check()
                self.right_counter += self.Ticket_2.check()
                self.right_counter += self.Ticket_3.check()
                self.right_counter += self.Ticket_4.check()
                self.right_counter += self.Ticket_5.check()
                self.right_counter += self.Ticket_6.check()
                self.right_counter += self.Ticket_7.check()
                self.right_counter += self.Ticket_8.check()
                self.finish_the_exam()
                window.destroy()
            else:
                window.destroy()
        
        btn_submit = ttk.Button(window, text="Проверить", command=check_access)
        btn_submit.pack(pady=25)
