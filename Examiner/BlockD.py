from tkinter import *
from tkinter import ttk

class BlockD(): 
    def __init__(self, notebook, position_question, position_answer):
        frame_5 = ttk.Frame(notebook)
        frame_5.pack(fill=BOTH, expand=True)
        notebook.add(frame_5, text="Вопросы: 22-25")
        self.selected = {1: 0, 2: 0, 3: 0, 4: 0}

        answers = ['ТСН', 'Тепло', 'ТС', 'ТЕП', 'т/c']
        selected_answer_1 = StringVar()
        self.label_question_1 = ttk.Label(frame_5, text="📌 Вопрос 22: Как корректно записывать слово: теплоснабжение в форме аббревиатуры?", font=("Times New Roman", 14, "bold"))
        self.label_question_1.pack(fill="x", pady=[25, 10], padx=10)

        def select_1(): 
            if selected_answer_1.get() == 'ТС':
                self.selected[1] = 1
            else:
                self.selected[1] = 0

        for item in answers:
            item_btn = ttk.Radiobutton(frame_5, text=item, variable=selected_answer_1, value=item, command=select_1)
            item_btn.pack(**position_answer)

        self.enabled_1 = IntVar()
        self.enabled_2 = IntVar()
        self.enabled_3 = IntVar()
        self.enabled_4 = IntVar()
        self.enabled_5 = IntVar()

        def select_3():
            if all([self.enabled_2.get(), self.enabled_1.get()]):
                self.selected[3] = 1
            else:
                self.selected[3] = 0

        self.label_question_2 = ttk.Label(frame_5, text="📌 Вопрос 23: При отключении котельной от э/э, газа или ХВС кому необходимо сообщить согласно регламенту?", font=("Times New Roman", 14, "bold"), wraplength=830)
        self.label_question_2.pack(fill="x", pady=[25, 10], padx=10)
        checkbutton_1 = ttk.Checkbutton(frame_5, text="Руководящий состав", variable=self.enabled_1, command=select_3)
        checkbutton_1.pack(**position_answer)
        checkbutton_2 = ttk.Checkbutton(frame_5, text="ЕДДС", variable=self.enabled_2, command=select_3)
        checkbutton_2.pack(**position_answer)
        checkbutton_3 = ttk.Checkbutton(frame_5, text="РСО", variable=self.enabled_3, command=select_3)
        checkbutton_3.pack(**position_answer)
        checkbutton_4 = ttk.Checkbutton(frame_5, text="Министерство энергетики и ЖКХ", variable=self.enabled_4, command=select_3)
        checkbutton_4.pack(**position_answer)
        checkbutton_5 = ttk.Checkbutton(frame_5, text="Минстрой РФ", variable=self.enabled_5, command=select_3)
        checkbutton_5.pack(**position_answer)

        answers = ['Каждые 2 часа', 'Каждые 30 минут', 'Каждый час', 'Не отслеживается', 'Ожидать, как только передадут сами']
        selected_answer_2 = StringVar()
        self.label_question_3 = ttk.Label(frame_5, text="📌 Вопрос 24: При отключении котельной от э/э, газа или ХВС, как часто необходимо отслеживать состояние и статус работ?", font=("Times New Roman", 14, "bold"), wraplength=770)
        self.label_question_3.pack(fill="x", pady=[25, 10], padx=10)

        def select_2(): 
            if selected_answer_2.get() == 'Каждые 30 минут':
                self.selected[2] = 1 
            else:
                self.selected[2] = 0

        for item in answers:
            item_btn = ttk.Radiobutton(frame_5, text=item, variable=selected_answer_2, value=item, command=select_2)
            item_btn.pack(**position_answer)
   
        self.enabled_6 = IntVar()
        self.enabled_7 = IntVar()
        self.enabled_8 = IntVar()

        def select_4():
            if all([self.enabled_6.get(), self.enabled_7.get(), self.enabled_8.get()]):
                self.selected[4] = 1
            else:
                self.selected[4] = 0

        self.label_question_4 = ttk.Label(frame_5, text="📌 Вопрос 25: Что в обязательном порядке нужно записать в журнал при телефонном звонке в ходе уточнения/сборе информации по инциденту у ЕДДС или РСО?", font=("Times New Roman", 14, "bold"), wraplength=830)
        self.label_question_4.pack(fill="x", pady=[25, 10], padx=10)
        checkbutton_6 = ttk.Checkbutton(frame_5, text="Дату и время звонка", variable=self.enabled_6, command=select_4)
        checkbutton_6.pack(**position_answer)
        checkbutton_7 = ttk.Checkbutton(frame_5, text="Должность собеседника", variable=self.enabled_7, command=select_4)
        checkbutton_7.pack(**position_answer)
        checkbutton_8 = ttk.Checkbutton(frame_5, text="Ф.И.О. собеседника", variable=self.enabled_8, command=select_4)
        checkbutton_8.pack(**position_answer)

    def check(self): 
        right_counter = 0

        if self.selected[1] == 1:
            right_counter += 1
            self.label_question_1.configure(foreground="#5c9682")
        else:
            self.label_question_1.configure(foreground="#CD5C5C")
        
        if self.selected[2] == 1:
            right_counter += 1
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.label_question_3.configure(foreground="#CD5C5C")

        if self.selected[3] == 1:
            right_counter += 1
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.label_question_2.configure(foreground="#CD5C5C")
        
        if self.selected[4] == 1:
            right_counter += 1
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.label_question_4.configure(foreground="#CD5C5C")

        return right_counter
    