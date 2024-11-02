from tkinter import *
from tkinter import ttk

class BlockB():
    def __init__(self, notebook, position_question, position_answer):
        frame_3 = ttk.Frame(notebook)
        frame_3.pack(fill=BOTH, expand=True)
        notebook.add(frame_3, text="Вопросы: 10-16")
        self.selected = 0

        self.label_question_1 = ttk.Label(frame_3, text="📌 Вопрос 10: Перечислите фамилии тех, кому отправлять информацию по отключению котельной от э/э (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=790)
        self.label_question_1.pack(**position_question)
        self.text_answer_1 = Text(frame_3, font=("Times New Roman", 14), width=75, height=2, wrap='word')
        self.text_answer_1.pack(**position_answer)

        self.label_question_2 = ttk.Label(frame_3, text="📌 Вопрос 11: Перечислите фамилии тех, кому отправлять информацию по отключению котельной от газа (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_2.pack(**position_question)
        self.text_answer_2 = Text(frame_3, font=("Times New Roman", 14), width=75, height=2, wrap='word')
        self.text_answer_2.pack(**position_answer)

        self.label_question_3 = ttk.Label(frame_3, text="📌 Вопрос 12: Перечислите фамилии тех, кому отправлять информацию по отключению котельной от ХВС (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_3.pack(**position_question)
        self.entry_answer_3 = ttk.Entry(frame_3, font=("Times New Roman", 14), width=80)
        self.entry_answer_3.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_3, text="📌 Вопрос 13: Перечислите фамилии тех, кому отправлять информацию по отключению потребителей от теплоснабжения или горячего водоснабжения (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_3, font=("Times New Roman", 14), width=80)
        self.entry_answer_4.pack(**position_answer)

        self.label_question_5 = ttk.Label(frame_3, text="📌 Вопрос 14: Перечислите фамилии тех, кому отправлять информацию по отключению потребителей от холодного водоснабжения (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_5.pack(**position_question)
        self.entry_answer_5 = ttk.Entry(frame_3, font=("Times New Roman", 14), width=80)
        self.entry_answer_5.pack(**position_answer)

        self.label_question_6 = ttk.Label(frame_3, text="📌 Вопрос 15: Напишите фамилии тех, кому отправлять информацию по отключению потребителей от теплоснабжения или горячего водоснабжения при более 10 ж/домов (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_6.pack(**position_question)
        self.entry_answer_6 = ttk.Entry(frame_3, font=("Times New Roman", 14), width=50)
        self.entry_answer_6.pack(**position_answer)

        answers = ['Да', 'Нет']
        selected_answer = StringVar()
        self.label_question_7 = ttk.Label(frame_3, text="📌 Вопрос 16: Имеем ли мы право представляться в ходе телефонного звонка как Министерство энергетики и ЖКХ по Самарской области?", font=("Times New Roman", 14, "bold"), wraplength=780)
        self.label_question_7.pack(fill="x", pady=[25, 10], padx=10)

        def select(): 
            if selected_answer.get() == 'Да':
                self.selected = 1
            else:
                self.selected = 0

        for item in answers:
            item_btn = ttk.Radiobutton(frame_3, text=item, variable=selected_answer, value=item, command=select)
            item_btn.pack(**position_answer)

    def check(self): 
        right_counter = 0

        check_sets = {1: {'шамаев', 'копылов', 'бахметов', 'ткачев', 'темирбулатов', 'малышев', 'гадалин', 'левин', 'атаев', 'балицкая', 'абрамчев', 'кирпичева'},
                      2: {'копылов', 'бахметов', 'ткачев', 'темирбулатов', 'малышев', 'гадалин', 'левин', 'атаев', 'балицкая', 'абрамчев', 'кирпичева'}, 
                      3: {'ткачев', 'темирбулатов', 'малышев', 'гадалин', 'левин', 'атаев', 'балицкая', 'абрамчев', 'кирпичева'},
                      4: {'ткачев', 'темирбулатов', 'малышев', 'атаев', 'балицкая', 'абрамчев', 'кирпичева'},
                      5: {'спицын', 'николаев', 'ткачев', 'темирбулатов', 'малышев', 'абрамчев', 'кирпичева'},
                      6: {'гадалин', 'левин'}}
        if set(i.lower() for i in self.text_answer_1.get("1.0", "end").split()) == check_sets[1]:
            right_counter += 1
            self.text_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#5c9682")
        else:
            self.text_answer_1.configure(state='disabled')
            self.label_question_1.configure(foreground="#CD5C5C")

        if set(i.lower() for i in self.text_answer_2.get("1.0", "end").split()) == check_sets[2]:
            right_counter += 1
            self.text_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#5c9682")
        else:
            self.text_answer_2.configure(state='disabled')
            self.label_question_2.configure(foreground="#CD5C5C")

        if set(i.lower() for i in self.entry_answer_3.get().split()) == check_sets[3]:
            right_counter += 1
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.entry_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#CD5C5C")

        if set(i.lower() for i in self.entry_answer_4.get().split()) == check_sets[4]:
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")

        if set(i.lower() for i in self.entry_answer_5.get().split()) == check_sets[5]:
            right_counter += 1
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#5c9682")
        else:
            self.entry_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground='#CD5C5C')
                                            
        if set(i.lower() for i in self.entry_answer_6.get().split()) == check_sets[6]:
            right_counter += 1
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#5c9682")
        else:
            self.entry_answer_6.configure(state='disabled')
            self.label_question_6.configure(foreground="#CD5C5C")

        if self.selected == 1:
            right_counter += 1
            self.label_question_7.configure(foreground="#5c9682")
        else:
            self.label_question_7.configure(foreground="#CD5C5C")

        return right_counter
    