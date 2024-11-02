from tkinter import *
from tkinter import ttk

class BlockA():
    def __init__(self, notebook, position_question, position_answer):
        frame_2 = ttk.Frame(notebook)
        frame_2.pack(fill=BOTH, expand=True)
        notebook.add(frame_2, text="Вопросы: 1-9")

        self.label_question_1 = ttk.Label(frame_2, text="📌 Вопрос 1: Начальник службы КИПиА это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_1.pack(**position_question)
        self.entry_answer_1 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_1.pack(**position_answer)

        self.label_question_2 = ttk.Label(frame_2, text="📌 Вопрос 2: Начальник газовой службы это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_2.pack(**position_question)
        self.entry_answer_2 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_2.pack(**position_answer)

        self.label_question_3 = ttk.Label(frame_2, text="📌 Вопрос 3: Начальник службы энергетики это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_3.pack(**position_question)
        self.entry_answer_3 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_3.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_2, text="📌 Вопрос 4: Главный теплоэнергетик это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_4.pack(**position_answer)

        self.label_question_5 = ttk.Label(frame_2, text="📌 Вопрос 5: Начальник управления эксплуатации это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_5.pack(**position_question)
        self.entry_answer_5 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_5.pack(**position_answer)

        self.label_question_6 = ttk.Label(frame_2, text="📌 Вопрос 6: Главный инженер это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_6.pack(**position_question)
        self.entry_answer_6 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_6.pack(**position_answer)

        self.label_question_7 = ttk.Label(frame_2, text="📌 Вопрос 7: Генеральный директор ООО «СамРЭК-Эксплуатация» это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_7.pack(**position_question)
        self.entry_answer_7 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_7.pack(**position_answer)

        self.label_question_8 = ttk.Label(frame_2, text="📌 Вопрос 8: Технический директор ООО «СамРЭК-Эксплуатация» это (только фамилия)?", font=("Times New Roman", 14, "bold"))
        self.label_question_8.pack(**position_question)
        self.entry_answer_8 = ttk.Entry(frame_2, font=("Times New Roman", 14), width=50)
        self.entry_answer_8.pack(**position_answer)

        self.label_question_9 = ttk.Label(frame_2, text="📌 Вопрос 9: Перечислите фамилии начальников участков (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"))
        self.label_question_9.pack(**position_question)
        self.text_answer_9 = Text(frame_2, font=("Times New Roman", 14), width=75, height=2, wrap='word')
        self.text_answer_9.pack(**position_answer)

    def check(self): 
        right_counter = 0
        
        if self.entry_answer_1.get().lower() == 'кувин':
            self.entry_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#5c9682")
            right_counter += 1
        else:        
            self.entry_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#CD5C5C")

        if self.entry_answer_2.get().lower() == 'копылов':
            right_counter += 1
            self.entry_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.entry_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#CD5C5C")

        if self.entry_answer_3.get().lower() == 'шамаев':
            right_counter += 1
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#CD5C5C")

        if self.entry_answer_4.get().lower() == 'атаев':
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")

        if self.entry_answer_5.get().lower() == 'темирбулатов':
            right_counter += 1
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#5c9682")
        else:
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#CD5C5C")

        if self.entry_answer_6.get().lower() == 'малышев':
            right_counter += 1
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#5c9682")
        else:
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#CD5C5C")

        if self.entry_answer_7.get().lower() == 'гадалин':
            right_counter += 1
            self.entry_answer_7.configure(state='disabled')
            self.label_question_7.configure(foreground="#5c9682")
        else:
            self.entry_answer_7.configure(state='disabled')
            self.label_question_7.configure(foreground="#CD5C5C")

        if self.entry_answer_8.get().lower() == 'левин':
            right_counter += 1
            self.entry_answer_8.configure(state='disabled')
            self.label_question_8.configure(foreground="#5c9682")
        else:
            self.entry_answer_8.configure(state='disabled')
            self.label_question_8.configure(foreground="#CD5C5C")

        check_set = {'козлов', 'карасев', 'ставин', 'карпекин', 'петров', 'казарин', 'уколов', 'широков', 'клякун', 'симонов'} 
        if set(i.lower() for i in self.text_answer_9.get("1.0", "end").split()) == check_set:
            right_counter += 1
            self.text_answer_9.configure(state='disabled')
            self.label_question_9.configure(foreground="#5c9682")
        else:
            self.text_answer_9.configure(state='disabled')
            self.label_question_9.configure(foreground="#CD5C5C")

        return right_counter
    