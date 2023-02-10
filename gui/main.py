import os
import sys
from shutil import rmtree
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from os.path import *

sys.path.append("../chal_types")
from chal_types import logger

from jinja2 import Template
from .popup import PopUpWindow
import re

yaml_template = """- {yaml_tag}
  name: {name}
  flag: "{flag}"
  config:{config}
"""
sub_chal_template = """
    chals:{% for chal in chals %}
      {{ '- ' + chal }}{% endfor %}
"""


class App(tk.Tk):
    coords = (-1, -1)
    challenges = {}

    def __init__(self, out_dir):
        super().__init__()
        theme_path = join(os.getcwd(), 'gui', 'sun-valley.tcl')
        self.tk.call("source", theme_path)
        self.tk.call("set_theme", "light")
        self.out_dir = out_dir

        self.side_frame = ttk.Frame(self)
        self.side_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas = tk.Canvas(self, width=1000, height=500, bg='#EEEEEE',
                                highlightthickness=5, highlightbackground="#DDDDDD")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.title("Challenge Generation GUI")
        button_frame = ttk.Frame(self)
        text_to_commands = [("Insert Entrypoint", self.insert_entrypoint),
                            ("Insert Challenge", self.insert_chal), ("Generate Competition Files", self.generate_files)]
        for text, command in text_to_commands:
            button = ttk.Button(button_frame, text=text,
                                command=command, style="Accent.TButton")
            button.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X, expand=True)
        button_frame.pack(fill=tk.X)

        self.canvas.bind('<1>', self.select_object)
        self.canvas.bind('<Shift-1>', self.make_line)
        self.canvas.bind('<Double-Button-1>', self.open_panel)
        self.insert_entrypoint()

    def make_line(self, event):
        x, y = event.x, event.y
        type_below = self.item_type(tk.CURRENT)
        if type_below == 'line':
            return
        if self.coords[0] == -1:
            self.coords = (x, y)
        line = self.canvas.create_line(
            self.coords[0], self.coords[1], x, y, width=5, arrow=tk.LAST)
        self.canvas.addtag_withtag('line', line)
        self.canvas.bind('<Shift-Motion>', self.finish_line)
        self.canvas.bind('<ButtonRelease-1>', self.exit_line)
        self.config(cursor='crosshair')

    def select_object(self, event):
        self.canvas.bind('<ButtonRelease-1>', self.deselect)
        self.bind('<BackSpace>', self.delete)
        self.close_panel(hold=True)
        old_item = self.item_type('selected')
        new_item = self.item_type(tk.CURRENT)
        if old_item == 'line':
            self.canvas.itemconfigure('selected', fill='black')
        else:
            self.canvas.itemconfigure('selected2', outline='black')
            self.canvas.dtag('selected2')
            self.canvas.bind('<Motion>', self.move_object)
            self.config(cursor='fleur')
        self.canvas.dtag('selected')
        if new_item == 'line':
            self.canvas.addtag_withtag('selected', tk.CURRENT)
            self.canvas.itemconfigure('selected', fill='orange')
        elif new_item == 'rectangle':
            self.canvas.addtag_withtag('selected2', tk.CURRENT)
            itemId = self.canvas.find_above(tk.CURRENT)[0]
            self.canvas.addtag_withtag('selected', itemId)
        else:
            self.canvas.addtag_withtag('selected', tk.CURRENT)
            item_id = self.canvas.find_below(tk.CURRENT)[0]
            self.canvas.addtag_withtag('selected2', item_id)
        self.canvas.itemconfigure('selected2', outline='orange')

    def close_panel(self, hold=False):
        for widgets in self.side_frame.winfo_children():
            widgets.destroy()
        if hold:
            hold_frame = ttk.Frame(self.side_frame, width=0, height=0)
            hold_frame.pack()

    def update_config(self, event):
        widget = event.widget
        val = widget.get()
        chal_name = self.canvas.itemcget('selected', 'text')
        if widget.var == 'name':
            if val in self.challenges and val != chal_name:
                logger.error('Challenge name already taken!')
                return
            self.challenges[val] = self.challenges.pop(chal_name)
            self.canvas.itemconfig('selected', text=val)
            fill = self.canvas.itemcget('selected2', 'fill')
            self.canvas.delete('selected2')
            self.create_bbox('selected', fill, tag='selected2')
        elif widget.var == 'flag':
            self.challenges[chal_name][1] = val

    def open_panel(self, event):
        def insert_config(label, text):
            flag_label = ttk.Label(self.side_frame, text=label)
            flag_label.pack(padx=10, pady=3)
            flag_text = ttk.Entry(self.side_frame, width=20)
            flag_text.var = label
            flag_text.bind("<FocusOut>", self.update_config)
            flag_text.insert(0, text)
            flag_text.pack(padx=10, pady=3)

        if self.item_type('selected') != 'text':
            return
        self.close_panel()
        self.unbind('<BackSpace>')
        chal_name = self.canvas.itemcget('selected', 'text')
        yaml_tag, flag, chal_class = self.challenges[chal_name]
        title_label = ttk.Label(self.side_frame, text=chal_class.__name__)
        title_label.pack(padx=10, pady=3)
        title_label.config(font=('Segoe UI', 14))
        insert_config("name", chal_name)
        insert_config("flag", flag)
        lines = chal_class.__doc__.split('\n')[5:-1]
        if 'None' in lines[0]:
            lines = []
        for line in lines:
            config_name = line.split('-')[0]
            config_name = re.sub(' ', '', config_name)
            insert_config(config_name, "")

    def item_type(self, id):
        try:
            self.canvas.itemcget(id, 'arrow')
            return 'line'
        except tk.TclError:
            try:
                self.canvas.itemcget(id, 'outline')
                return 'rectangle'
            except:
                return 'text'

    def move_object(self, event):
        if event.x < 0 or event.x > self.canvas.winfo_width() or event.y < 0 or event.y > self.canvas.winfo_height():
            return
        text_coords = self.canvas.coords('selected')
        rect_coords = self.canvas.coords('selected2')
        for obj in self.find_all('selected2'):
            if self.item_type(obj) == 'line':
                line_coords = self.canvas.coords(obj)
                if line_coords[2] >= rect_coords[0] and line_coords[2] <= rect_coords[2] and line_coords[3] >= rect_coords[1] and line_coords[3] <= rect_coords[3]:
                    line_coords[2] = line_coords[2] - text_coords[0] + event.x
                    line_coords[3] = line_coords[3] - text_coords[1] + event.y
                else:
                    line_coords[0] = line_coords[0] - text_coords[0] + event.x
                    line_coords[1] = line_coords[1] - text_coords[1] + event.y
                self.canvas.coords(obj, *line_coords)
        
        self.move(event, text_coords, 'selected')
        self.move(event, rect_coords, 'selected2')

    def move(self, event, coords, tag):
        if not coords:
            return
        elif len(coords) == 2:
            middle_x = coords[0]
            middle_y = coords[1]
        else:
            middle_x = abs((coords[0] + coords[2]) / 2)
            middle_y = abs((coords[1] + coords[3]) / 2)
        movex = event.x - middle_x
        movey = event.y - middle_y
        self.canvas.move(tag, movex, movey)

    def finish_line(self, event):
        x, y = event.x, event.y
        self.canvas.coords('line', self.coords[0], self.coords[1], x, y)

    def deselect(self, event):
        self.canvas.unbind('<Motion>')
        self.config(cursor='arrow')
        self.canvas.bind('<Shift-1>', self.make_line)

    def delete(self, event):
        item_type = self.item_type('selected')
        if item_type == 'text':
            name = self.canvas.itemcget('selected', 'text')
            self.challenges.pop(name, None)

        for item in self.canvas.find_all('selected2'):
            if(self.item_type(item) == 'line'):
                self.canvas.delete(item)
        self.canvas.delete('selected')
        self.canvas.delete('selected2')

    def exit_line(self, event):
        all_items = self.find_all('line')
        if all_items == None:
            return
        if len(all_items) == 1:
            self.canvas.delete('line')
        self.canvas.unbind('<Shift-Motion>')
        self.canvas.dtag('line')
        self.config(cursor='arrow')
        self.coords = (-1, -1)

    def create_bbox(self, text_id, fill, tag=None):
        bounds = list(self.canvas.bbox(text_id))
        bounds[0] -= 5
        bounds[1] -= 5
        bounds[2] += 5
        bounds[3] += 5
        r = self.canvas.create_rectangle(bounds, fill=fill, tags=tag)
        self.canvas.tag_lower(r, text_id)

    def insert_entrypoint(self):
        self.insert_chal(entrypoint=True)

    def insert_chal(self, entrypoint=False):
        p = PopUpWindow(self, entrypoint)
        self.wait_window(p)
        name, yaml_tag, flag, chal_class = self.challenge
        if name in self.challenges:
            messagebox.showerror('Error!', 'Challenge already exists!')
            return
        self.challenges[name] = [yaml_tag, flag, chal_class]
        if entrypoint:
            tag = 'entrypoint'
            fill = 'lightblue'
        else:
            tag = None
            fill = 'white'
        t = self.canvas.create_text(
            525, 262.5, text=name, fill='black', width=100, tags=tag)
        self.create_bbox(t, fill)
        delattr(self, 'challenge')

    def find_all(self, item_id):
        coords = self.canvas.coords(item_id)
        if len(coords) == 0:
            return
        if self.item_type(item_id) == 'line':
            coords = coords[2:]
            second_coords = [coords[0] + 1, coords[1] + 1]
            coords.extend(second_coords)
        return list(self.canvas.find_overlapping(*coords))

    def generate_files(self):
        yaml_files = []

        def traverse(itemid):
            all_items = self.find_all(itemid)
            sub_chals = []
            config = ""
            for item in all_items:
                item_type = self.item_type(item)
                if item_type == 'line':
                    new_node = self.find_all(item)
                    if itemid in new_node:
                        continue
                    for new_item in new_node:
                        new_item_type = self.item_type(new_item)
                        if new_item_type == 'rectangle':
                            traverse(new_item)
                        elif new_item_type == 'text':
                            name = self.canvas.itemcget(new_item, 'text')
                            sub_chals.append(name)
                elif item_type == 'text':
                    title = self.canvas.itemcget(item, 'text')
            if sub_chals:
                config = Template(sub_chal_template).render(chals=sub_chals)
            chal_tag, flag, class_name = self.challenges[title]
            yaml_formatted = yaml_template.format(
                name=title, yaml_tag=chal_tag, flag=flag, config=config)
            yaml_files.append((title, yaml_formatted))
            return sub_chals

        entry = self.canvas.find_below('entrypoint')
        try:
            traverse(entry)
        except RecursionError:
            logger.error('Arrow loop detected! Please try again.')
            return
        except TypeError:
            logger.error('Please make sure you have an entrypoint!')
            return
        entry_title = self.canvas.itemcget('entrypoint', 'text')

        competition_out = join(os.getcwd(), self.out_dir)
        if exists(competition_out):
            rmtree(competition_out)
        os.makedirs(competition_out)
        with open(join(competition_out, 'config.yaml'), 'w') as w:
            w.write(f'Entrypoint: {entry_title}')
        for file in yaml_files:
            folder_name, yaml = file
            folder = join(competition_out, 'chals', folder_name)
            os.makedirs(folder)
            with open(join(folder, 'chal.yaml'), 'w') as w:
                w.write(yaml)
