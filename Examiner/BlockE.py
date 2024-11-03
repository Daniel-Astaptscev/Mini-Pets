from tkinter import *
from tkinter import ttk

class BlockE(): 
    def __init__(self, notebook, position_question, position_answer):
        frame_6 = ttk.Frame(notebook)
        frame_6.pack(fill=BOTH, expand=True)
        notebook.add(frame_6, text="Вопросы: 26-30")
        self.selected = 0

        self.label_question_1 = ttk.Label(frame_6, text="📌 Вопрос 26: Напишите количество объектов входящих в состав группы компаний СамРЭК (число)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_1.pack(**position_question)
        self.spinbox_answer_1 = ttk.Spinbox(frame_6, from_=1, to=350, font=("Times New Roman", 14))
        self.spinbox_answer_1.pack(**position_answer)

        self.label_question_2 = ttk.Label(frame_6, text="📌 Вопрос 27: Напишите количество котельных ГВС (число)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_2.pack(**position_question)
        self.spinbox_answer_2 = ttk.Spinbox(frame_6, from_=1, to=150, font=("Times New Roman", 14))
        self.spinbox_answer_2.pack(**position_answer)

        self.enabled_1 = IntVar()
        self.enabled_2 = IntVar()
        self.enabled_3 = IntVar()
        self.enabled_4 = IntVar()
        self.enabled_5 = IntVar()
        self.enabled_6 = IntVar()
        self.enabled_7 = IntVar()
        self.enabled_8 = IntVar()
        self.enabled_9 = IntVar()
        self.enabled_10 = IntVar()
        self.enabled_11 = IntVar()
        self.enabled_12 = IntVar()
        self.enabled_13 = IntVar()
        self.enabled_14 = IntVar()

        def select():
            if all([self.enabled_1.get(), self.enabled_2.get(), self.enabled_3.get(), self.enabled_4.get(), self.enabled_5.get(), self.enabled_6.get(), self.enabled_7.get(), self.enabled_8.get(), self.enabled_9.get(), self.enabled_11.get(), self.enabled_12.get()]):
                self.selected = 1
            else:
                self.selected = 0

        self.label_question_3 = ttk.Label(frame_6, text="📌 Вопрос 28: Какие участки есть в организации ООО СамРЭК?", font=("Times New Roman", 14, "bold"))
        self.label_question_3.pack(**position_question)
        checkbutton_1 = ttk.Checkbutton(frame_6, text="1", variable=self.enabled_1, command=select)
        checkbutton_1.pack(**position_answer)
        checkbutton_2 = ttk.Checkbutton(frame_6, text="2", variable=self.enabled_2, command=select)
        checkbutton_2.pack(**position_answer)
        checkbutton_3 = ttk.Checkbutton(frame_6, text="3", variable=self.enabled_3, command=select)
        checkbutton_3.pack(**position_answer)
        checkbutton_4 = ttk.Checkbutton(frame_6, text="4", variable=self.enabled_4, command=select)
        checkbutton_4.pack(**position_answer)
        checkbutton_5 = ttk.Checkbutton(frame_6, text="5", variable=self.enabled_5, command=select)
        checkbutton_5.pack(**position_answer)
        checkbutton_6 = ttk.Checkbutton(frame_6, text="6", variable=self.enabled_6, command=select)
        checkbutton_6.pack(**position_answer)
        checkbutton_7 = ttk.Checkbutton(frame_6, text="7", variable=self.enabled_7, command=select)
        checkbutton_7.pack(**position_answer)
        checkbutton_8 = ttk.Checkbutton(frame_6, text="8", variable=self.enabled_8, command=select)
        checkbutton_8.pack(**position_answer)
        checkbutton_9 = ttk.Checkbutton(frame_6, text="9", variable=self.enabled_9, command=select)
        checkbutton_9.pack(**position_answer)
        checkbutton_10 = ttk.Checkbutton(frame_6, text="10", variable=self.enabled_10, command=select)
        checkbutton_10.pack(**position_answer)
        checkbutton_11 = ttk.Checkbutton(frame_6, text="11", variable=self.enabled_11, command=select)
        checkbutton_11.pack(**position_answer)
        checkbutton_12 = ttk.Checkbutton(frame_6, text="12", variable=self.enabled_12, command=select)
        checkbutton_12.pack(**position_answer)
        checkbutton_13 = ttk.Checkbutton(frame_6, text="13", variable=self.enabled_13, command=select)
        checkbutton_13.pack(**position_answer)
        checkbutton_14 = ttk.Checkbutton(frame_6, text="14", variable=self.enabled_14, command=select)
        checkbutton_14.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_6, text="📌 Вопрос 29: Как расшифровывается аббревиатура ТМ (одно слово)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_6, font=("Times New Roman", 14), width=50)
        self.entry_answer_4.pack(**position_answer)

        self.label_question_5 = ttk.Label(frame_6, text="📌 Вопрос 30: Как расшифровывается аббревиатура ПГ (два слова)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_5.pack(**position_question)
        self.entry_answer_5 = ttk.Entry(frame_6, font=("Times New Roman", 14), width=50)
        self.entry_answer_5.pack(**position_answer)

    def check(self): 
        right_counter = 0

        if self.spinbox_answer_1.get() == '213':
            right_counter += 1
            self.spinbox_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#5c9682")
        else:
            self.spinbox_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#CD5C5C")

        if self.spinbox_answer_2.get() == '23':
            right_counter += 1
            self.spinbox_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.spinbox_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#CD5C5C")

        if self.entry_answer_4.get().lower() == 'тепломеханика':
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")

        if self.entry_answer_5.get().lower() == 'пожарный гидрант':
            right_counter += 1
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#5c9682")
        else:
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#CD5C5C")

        if self.selected == 1:
            right_counter += 1
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.label_question_3.configure(foreground="#CD5C5C")

        return right_counter
    