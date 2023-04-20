from chal_types import ChallengeEnvironment, GeneratedChallenge, challenge_types
import sys
import tkinter as tk
from os.path import *
from tkinter import messagebox, ttk

sys.path.insert(0, dirname(dirname(abspath(__file__))))

all_challenges = {}
environments = {}
for subclass in GeneratedChallenge.__subclasses__():
    if subclass.__name__ != 'ChallengeEnvironment':
        all_challenges[subclass.__name__] = subclass.yaml_tag
for subclass in ChallengeEnvironment.__subclasses__():
    environments[subclass.__name__] = subclass.yaml_tag
all_challenges.update(environments)


class PopUpWindow(tk.Toplevel):
    def __init__(self, master, entrypoint):
        self.master = master
        super().__init__(master)
        self.grab_set()

        self.minsize(300, 100)
        self.transient(self.master)

        x = master.winfo_x()
        y = master.winfo_y()
        self.geometry(f"+{x+400}+{y+250}")

        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.title(f'Insert {"Entrypoint" if entrypoint else "Challenge"}')

        name_label = ttk.Label(self, text='Name')
        name_label.pack()

        self.name = ttk.Entry(self, width=23)
        self.name.pack()

        type_label = ttk.Label(self, text='Type')
        type_label.pack()

        combo_list = environments if entrypoint else all_challenges
        combo_list = list(combo_list)
        combo_list.sort()
        self.type_selector = ttk.Combobox(
            self, values=combo_list, state='readonly')
        self.type_selector.pack()

        flag_label = ttk.Label(self, text="Flag")
        flag_label.pack()

        self.flag = ttk.Entry(self, width=23)
        self.flag.pack()

        insert_button = ttk.Button(
            self, text="Insert", command=self.close_window, style="Toggle.TButton")
        insert_button.pack(pady=10)

    def close_window(self):
        name_out = self.name.get()
        type_out = self.type_selector.get()
        flag_out = self.flag.get()
        if name_out == '' or type_out == '' or flag_out == '':
            messagebox.showerror("Error", "Please make a valid selection!")
        else:
            self.master.challenge = (
                name_out, all_challenges[type_out], flag_out, challenge_types[type_out])
            self.grab_release()
            self.destroy()
            self.master.deiconify()
