from tkinter import *
from tkinter import ttk

class BlockF(): 
    def __init__(self, notebook, position_question, position_answer):
        frame_7 = ttk.Frame(notebook)
        frame_7.pack(fill=BOTH, expand=True)
        notebook.add(frame_7, text="Вопросы: 31-34")
        self.selected = {1: 0, 2: 0, 3: 0}

        self.enabled_1 = IntVar()
        self.enabled_2 = IntVar()
        self.enabled_3 = IntVar()
        self.enabled_4 = IntVar()
        self.enabled_5 = IntVar()
        self.enabled_6 = IntVar()
        
        def select_1():
            if all([self.enabled_1.get(), self.enabled_2.get(), self.enabled_3.get(), self.enabled_4.get()]):
                self.selected[1] = 1
            else:
                self.selected[1] = 0

        self.label_question_1 = ttk.Label(frame_7, text="📌 Вопрос 31: Какие сферы ЖКХ обслуживает ООО СамРЭК?", font=("Times New Roman", 14, "bold"), wraplength=830)
        self.label_question_1.pack(fill="x", pady=[25, 10], padx=10)
        checkbutton_1 = ttk.Checkbutton(frame_7, text="Холодное водоснабжение", variable=self.enabled_1, command=select_1)
        checkbutton_1.pack(**position_answer)
        checkbutton_2 = ttk.Checkbutton(frame_7, text="Горячее водоснабжение", variable=self.enabled_2, command=select_1)
        checkbutton_2.pack(**position_answer)
        checkbutton_3 = ttk.Checkbutton(frame_7, text="Теплоснабжение", variable=self.enabled_3, command=select_1)
        checkbutton_3.pack(**position_answer)
        checkbutton_4 = ttk.Checkbutton(frame_7, text="Водоотведение", variable=self.enabled_4, command=select_1)
        checkbutton_4.pack(**position_answer)
        checkbutton_5 = ttk.Checkbutton(frame_7, text="Электроснабжение", variable=self.enabled_5, command=select_1)
        checkbutton_5.pack(**position_answer)
        checkbutton_6 = ttk.Checkbutton(frame_7, text="Газоснабжение", variable=self.enabled_6, command=select_1)
        checkbutton_6.pack(**position_answer)

        self.enabled_7 = IntVar()
        self.enabled_8 = IntVar()
        self.enabled_9 = IntVar()
        self.enabled_10 = IntVar()
        self.enabled_11 = IntVar()
        self.enabled_12 = IntVar()

        def select_2():
            if all([self.enabled_8.get(), self.enabled_9.get()]):
                self.selected[2] = 1
            else:
                self.selected[2] = 0

        self.label_question_2 = ttk.Label(frame_7, text="📌 Вопрос 32: Какие сферы ЖКХ обслуживает ООО СамРЭК-Тепло Жигулевск?", font=("Times New Roman", 14, "bold"), wraplength=830)
        self.label_question_2.pack(fill="x", pady=[25, 10], padx=10)
        checkbutton_7 = ttk.Checkbutton(frame_7, text="Холодное водоснабжение", variable=self.enabled_7, command=select_2)
        checkbutton_7.pack(**position_answer)
        checkbutton_8 = ttk.Checkbutton(frame_7, text="Горячее водоснабжение", variable=self.enabled_8, command=select_2)
        checkbutton_8.pack(**position_answer)
        checkbutton_9 = ttk.Checkbutton(frame_7, text="Теплоснабжение", variable=self.enabled_9, command=select_2)
        checkbutton_9.pack(**position_answer)
        checkbutton_10 = ttk.Checkbutton(frame_7, text="Водоотведение", variable=self.enabled_10, command=select_2)
        checkbutton_10.pack(**position_answer)
        checkbutton_11 = ttk.Checkbutton(frame_7, text="Электроснабжение", variable=self.enabled_11, command=select_2)
        checkbutton_11.pack(**position_answer)
        checkbutton_12 = ttk.Checkbutton(frame_7, text="Газоснабжение", variable=self.enabled_12, command=select_2)
        checkbutton_12.pack(**position_answer)

        self.enabled_13 = IntVar()
        self.enabled_14 = IntVar()
        self.enabled_15 = IntVar()
        self.enabled_16 = IntVar()
        self.enabled_17 = IntVar()
        self.enabled_18 = IntVar()

        def select_3():
            if all([self.enabled_8.get(), self.enabled_9.get()]):
                self.selected[3] = 1
            else:
                self.selected[3] = 0

        self.label_question_3 = ttk.Label(frame_7, text="📌 Вопрос 33: Какие сферы ЖКХ обслуживает ООО СамРЭК-Нефтегорск?", font=("Times New Roman", 14, "bold"), wraplength=830)
        self.label_question_3.pack(fill="x", pady=[25, 10], padx=10)
        checkbutton_13 = ttk.Checkbutton(frame_7, text="Холодное водоснабжение", variable=self.enabled_13, command=select_3)
        checkbutton_13.pack(**position_answer)
        checkbutton_14 = ttk.Checkbutton(frame_7, text="Горячее водоснабжение", variable=self.enabled_14, command=select_3)
        checkbutton_14.pack(**position_answer)
        checkbutton_15 = ttk.Checkbutton(frame_7, text="Теплоснабжение", variable=self.enabled_15, command=select_3)
        checkbutton_15.pack(**position_answer)
        checkbutton_16 = ttk.Checkbutton(frame_7, text="Водоотведение", variable=self.enabled_16, command=select_3)
        checkbutton_16.pack(**position_answer)
        checkbutton_17 = ttk.Checkbutton(frame_7, text="Электроснабжение", variable=self.enabled_17, command=select_3)
        checkbutton_17.pack(**position_answer)
        checkbutton_18 = ttk.Checkbutton(frame_7, text="Газоснабжение", variable=self.enabled_18, command=select_3)
        checkbutton_18.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_7, text="📌 Вопрос 34: Как расшифровывается аббревиатура ВК (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_7, font=("Times New Roman", 14), width=50)
        self.entry_answer_4.pack(**position_answer)

    def check(self): 
        right_counter = 0

        if self.entry_answer_4.get().lower() == 'водопроводный колодец' or self.entry_answer_4.get().lower() == 'водопроводная камера':
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")

        if self.selected[1] == 1:
            right_counter += 1
            self.label_question_1.configure(foreground="#5c9682")
        else:
            self.label_question_1.configure(foreground="#CD5C5C")

        if self.selected[2] == 1:
            right_counter += 1
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.label_question_2.configure(foreground="#CD5C5C")

        if self.selected[3] == 1:
            right_counter += 1
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.label_question_3.configure(foreground="#CD5C5C")

        return right_counter
    