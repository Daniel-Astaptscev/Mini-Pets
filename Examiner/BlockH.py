from tkinter import *
from tkinter import ttk

class BlockH(): 
    def __init__(self, notebook, position_question, position_answer):
        frame_9 = ttk.Frame(notebook)
        frame_9.pack(fill=BOTH, expand=True)
        notebook.add(frame_9, text="Вопросы: 39-44")

        self.label_question_1 = ttk.Label(frame_9, text="📌 Вопрос 39: Как расшифровывается аббревиатура ЛЭП (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_1.pack(**position_question)
        self.entry_answer_1 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_1.pack(**position_answer)

        self.label_question_2 = ttk.Label(frame_9, text="📌 Вопрос 40: Как расшифровывается аббревиатура КК (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_2.pack(**position_question)
        self.entry_answer_2 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_2.pack(**position_answer)

        self.label_question_3 = ttk.Label(frame_9, text="📌 Вопрос 41: Как расшифровывается аббревиатура УК (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_3.pack(**position_question)
        self.entry_answer_3 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_3.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_9, text="📌 Вопрос 42: Как расшифровывается аббревиатура МП или МУП (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_4.pack(**position_answer)

        self.label_question_5 = ttk.Label(frame_9, text="📌 Вопрос 43: На каких эксплуатационных участках в группе компаний СамРЭК находятся диспетерские службы? (числа, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_5.pack(**position_question)
        self.entry_answer_5 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_5.pack(**position_answer)

        self.label_question_6 = ttk.Label(frame_9, text="📌 Вопрос 44: Как расшифровывается аббревиатура ЦТП (три слова)??", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_6.pack(**position_question)
        self.entry_answer_6 = ttk.Entry(frame_9, font=("Times New Roman", 14), width=50)
        self.entry_answer_6.pack(**position_answer)

    def check(self): 
        right_counter = 0

        if self.entry_answer_1.get().lower() == 'линия электропередач':
            right_counter += 1
            self.entry_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#5c9682")
        else:
            self.entry_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#CD5C5C")

        if self.entry_answer_2.get().lower() == 'канализационный коллектор' or self.entry_answer_2.get().lower() == 'кабельный колодец':
            right_counter += 1
            self.entry_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.entry_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#CD5C5C")

        if self.entry_answer_3.get().lower() == 'управляющая компания':
            right_counter += 1
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#CD5C5C")

        if self.entry_answer_4.get().lower() == 'муниципальное предприятие':
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")

        if '4' in self.entry_answer_5.get() and '6' in self.entry_answer_5.get() and '10' in self.entry_answer_5.get():
            right_counter += 1
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#5c9682")
        else:
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#CD5C5C")

        if self.entry_answer_6.get().lower() == 'центральный тепловой пункт':
            right_counter += 1
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#5c9682")
        else:
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#CD5C5C")

        return right_counter   
    