from tkinter import *

import data_migrate
import dsbayes
import str_carve
from dsbayes import TrainCont

root = Tk()
root.title("Midas")
root.geometry("500x500")


class Elder:
    separator: str = ","
    bayes: TrainCont

    def __init__(self, master):
        my_frame = Frame(master)
        my_frame.pack()
        self.button_create_bayes = Button(master, text="nowy bayes", command=self.create_bayes)
        self.button_create_bayes.pack()
        self.button_load_file = Button(master, text="trenuj z pliku", command=self.load_data)
        self.button_load_file.pack()
        self.button_test_file = Button(master, text="testuj plik", command=self.test_data)
        self.button_test_file.pack()
        self.button_man_test=Button(master,text="manualny test",command=self.man_test)
        self.button_man_test.pack()
        self.button_separator_ch = Button(master, text="zmien separator", command=self.set_separator)
        self.button_separator_ch.pack()
        self.promp_win = Text(root, height=200, width=200)
        self.promp_win.pack()

    def create_bayes(self):
        promp = self.get_prompt()
        try:
            dim = int(promp)
            if dim > 0:
                self.bayes = dsbayes.TrainCont(dim)
                self.say_board("poprawnie uworzony core")
            else:
                self.say_board("dim powinno byc wieksze niż 0")
        except ValueError:
            self.say_board("błąd parsowania")

    def load_data(self):
        if self.bayes is None:
            return
        promp = self.get_prompt()
        load_res = data_migrate.data_load(promp)
        if not load_res[0]:
            self.say_board("błąd ładowania pliku")
            return
        data_arar = str_carve.get_vecs(load_res[1], separator=self.separator)
        self.bayes.addRecs(data_arar)
        self.say_board("dane załadowane")

    def test_data(self):
        if self.bayes is None:
            return
        promp = self.get_prompt()
        load_res = data_migrate.data_load(promp)
        if not load_res[0]:
            self.say_board("błąd ładowania pliku")
            return
        res = self.bayes.testList(str_carve.get_vecs(load_res[1], separator=self.separator))
        if res is not None:
            self.say_board(res)
        else:
            self.say_board("błąd")

    def man_test(self):
        if self.bayes is None:
            return
        promp = self.get_prompt()
        tmp = str_carve.get_vecs(promp, separator=self.separator)
        res = self.bayes.testList(tmp)
        if res is not None:
            self.say_board(res)
        else:
            self.say_board("błąd")

    def get_prompt(self):
        return self.promp_win.get("1.0", "end-1c")

    def set_separator(self):
        self.separator = self.get_prompt()

    def clear_board(self):
        self.promp_win.delete(1.0, "end")

    def say_board(self, text_s):
        self.clear_board()
        self.promp_win.insert(1.0, text_s)


e = Elder(root)
root.mainloop()
