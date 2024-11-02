from tkinter import *
from tkinter import ttk

class BlockC(): 
    def __init__(self, notebook, position_question, position_answer):
        frame_4 = ttk.Frame(notebook)
        frame_4.pack(fill=BOTH, expand=True)
        notebook.add(frame_4, text="Вопросы: 17-21")
        self.selected = {1: 0, 2: 0}

        answers = ['24 часа', '36 часов', '8 часов', '48 часов']
        selected_answer_1 = StringVar()
        self.label_question_1 = ttk.Label(frame_4, text="📌 Вопрос 17: Какое количество времени должно пройти, чтобы было превышение по холодному водоснабжению?", font=("Times New Roman", 14, "bold"), wraplength=770)
        self.label_question_1.pack(fill="x", pady=[25, 10], padx=10)

        def select_1(): 
            if selected_answer_1.get() == '24 часа':
                self.selected[1] = 1
            else:
                self.selected[1] = 0
            
        for item in answers:
            item_btn = ttk.Radiobutton(frame_4, text=item, variable=selected_answer_1, value=item, command=select_1)
            item_btn.pack(**position_answer)

        answers = ['24 часа', '36 часов', '8 часов', '48 часов']
        selected_answer_2 = StringVar()
        self.label_question_2 = ttk.Label(frame_4, text="📌 Вопрос 18: Какое количество времени должно пройти, чтобы было превышение по теплоснабжению и горячему водоснабжению? ", font=("Times New Roman", 14, "bold"), wraplength=770)
        self.label_question_2.pack(fill="x", pady=[25, 10], padx=10)

        def select_2(): 
            if selected_answer_2.get() == '36 часов':
                self.selected[2] = 1
            else:
                self.selected[2] = 0

        for item in answers:
            item_btn = ttk.Radiobutton(frame_4, text=item, variable=selected_answer_2, value=item, command=select_2)
            item_btn.pack(**position_answer)

        self.label_question_3 = ttk.Label(frame_4, text="📌 Вопрос 19: Напишите количество отправлений информационной справки в течении суток (число)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_3.pack(**position_question)
        self.spinbox_answer_3 = ttk.Spinbox(frame_4, from_=1, to=15, font=("Times New Roman", 14))
        self.spinbox_answer_3.pack(**position_answer)

        self.label_question_4 = ttk.Label(frame_4, text="📌 Вопрос 20: Как корректно заменяется слово «порыв/авария/утечка» на трубопроводе (одно слово)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_4.pack(**position_question)
        self.entry_answer_4 = ttk.Entry(frame_4, font=("Times New Roman", 14), width=50)
        self.entry_answer_4.pack(**position_answer)

        self.label_question_5 = ttk.Label(frame_4, text="📌 Вопрос 21: Перечислите какие муниципальные районы или городские округа входят в группу компаний СамРЭК (без запятых, через пробел)?", font=("Times New Roman", 14, "bold"), wraplength=800)
        self.label_question_5.pack(**position_question)
        self.text_answer_5 = Text(frame_4, font=("Times New Roman", 14), width=80, height=5, wrap='word')
        self.text_answer_5.pack(**position_answer)

    def check(self): 
        right_counter = 0

        if self.spinbox_answer_3.get() == '5':
            right_counter += 1
            self.spinbox_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#5c9682")
        else:
            self.spinbox_answer_3.configure(state='disabled')
            self.label_question_3.configure(foreground="#CD5C5C")

        if self.entry_answer_4.get().lower() == 'повреждение':
            right_counter += 1
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#5c9682")
        else:
            self.entry_answer_4.configure(state='disabled')
            self.label_question_4.configure(foreground="#CD5C5C")
        
        check_set = {'исаклинский', 'кошкинский', 'елховский', 'ставропольский', 'безенчукский', 'большечерниговский', 'пестравский', 'хворостянский', 'волжский', 'кинельский', 'нефтегорский', 'похвистневский', 'похвистнево', 'кинель-Черкасский', 'приволжский', 'чапаевск', 'новокуйбышевск', 'самара', 'жигулевск', 'октябрьск', 'шигонский', 'богатовский', 'сергиевский'} 
        if set(i.lower() for i in self.text_answer_5.get("1.0", "end").split()) == check_set:
            right_counter += 1
            self.text_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#5c9682")
        else:
            self.text_answer_5.configure(state='disabled')
            self.label_question_5.configure(foreground="#CD5C5C")

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

        return right_counter
    