from tkinter import *
from tkinter import ttk
from StartPage import StartPage as MainPage

class Position():
    position_question = {'fill': 'x', 'padx': 10, 'pady': [25, 0]}
    position_answer = {'anchor': NW, 'padx': 38, 'pady': 5} 


if __name__ == "__main__":
    root = Tk()

    notebook = ttk.Notebook()
    notebook.pack(expand=True, fill=BOTH)

    StartPage = MainPage(notebook, Position.position_question, Position.position_answer)

    root.title("Examiner")
    root.geometry("850x930")
    icon = PhotoImage(file = "icon.png")
    root.iconphoto(True, icon)

    root.update_idletasks()
    width = root.winfo_width()
    frm_width = root.winfo_rootx() - root.winfo_x()
    root_width = width + 2 * frm_width
    height = root.winfo_height()
    titlebar_height = root.winfo_rooty() - root.winfo_y()
    root_height = height + titlebar_height + frm_width
    x = root.winfo_screenwidth() // 2 - root_width // 2
    y = root.winfo_screenheight() // 2 - root_height // 2
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.deiconify()

    root.mainloop()
