"""File with TableWindow class"""
import customtkinter
import customtkinter as ctk
import tkinter
from tkinter import ttk
from database.db import Database
from functions.funcs import is_float


class TableWindow(ctk.CTk):
    """This class manages opening all tables in application"""
    def __init__(self, parent: ctk.CTk, title: str) -> None:
        """Constructor of class"""
        super().__init__()
        self.title = title
        self.db_obj = Database()
        self.root = ctk.CTkToplevel(parent)
        self.root.title(title)
        self.root.resizable(False, False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        # Checking win type
        if title in ["computer_characteristics", "computers"]:
            self.draw_widgets_pair()
        else:
            self.draw_widgets()
        self.grab_focus()


    def set_style(self):
        """Method to set styles"""
        # Styles
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure(
            "Treeview.Heading",
            background="dodgerblue1",
            foreground="white",
            font=('Arial', 13, 'bold')
        )
        self.style.configure(
            "Treeview",
            fieldbackground="grey20",
            foreground="white",
            background="transparent"
        )
        self.style.map(
            "Treeview",
            background=[("selected", "disabled", "grey"), ("selected", "white")],
            foreground=[("selected", "disabled", "black"), ("selected", "black")]
        )
        self.style2 = ttk.Style()
        self.style2.theme_use("default")
        self.style2.configure(
            "TNotebook",
            background="grey20",
            tabposition="sw"
        )
        self.style2.configure(
            "TNotebook.Tab",
            background="dodgerblue1",
            foreground="white",
            font=('Arial', 10, 'bold')
        )
        self.style2.map(
            "TNotebook",
            background=[("selected", "blue")]
        )
        self.style2.map(
            "TNotebook.Tab",
            background=[("selected", "white")],
            foreground=[("selected", "black")]
        )

    def insert_data_into_db(self) -> None:
        """Method to insert data to database"""
        data = []
        keys = self.columns
        for entry in self.entries:
            if entry.get().isdigit():
                data.append(int(entry.get()))
            elif is_float(entry.get()):
                data.append(float(entry.get()))
            else:
                data.append(entry.get())
        data = str(tuple(data))
        keys = str(tuple(keys)).replace("'", "")
        print(self.db_obj.insert_data(self.title, data, keys))
        self.root.destroy()

    def delete_data_from_db(self) -> None:
        """Method to delete data from database"""
        key = self.key_find
        value = self.entry_delete.get()
        if value.isdigit():
            value = int(value)
            print(self.db_obj.delete_data(self.title, key, value))
        self.root.destroy()

    def delete_data_from_db_pair(self) -> None:
        """Method to delete data from database using pair of primary keys"""
        key1 = self.key_find[0]
        key2 = self.key_find[1]
        value1 = self.entry1_delete.get()
        value2 = self.entry2_delete.get()
        if value1.isdigit() and value1.isdigit():
            value1 = int(value1)
            value2 = int(value2)
            print(self.db_obj.delete_data_pair(self.title, key1, key2, value1, value2))
        self.root.destroy()

    def draw_widgets_pair(self) -> None:
        """Method to draw widgets 1"""
        self.set_style()
        # Tabs
        tab_control = ttk.Notebook(self.root)
        tab_table = ctk.CTkFrame(tab_control)
        tab_insertion = ctk.CTkFrame(tab_control)
        tab_delete = ctk.CTkFrame(tab_control)
        tab_control.add(tab_table, text="Table")
        tab_control.add(tab_insertion, text="Insert")
        tab_control.add(tab_delete, text="Delete")
        tab_control.pack(expand=1, fill="both")
        # Getting db data
        data = self.db_obj.get_table(self.title)
        self.columns = list(data[0].keys())
        # Db table
        tree = ttk.Treeview(master=tab_table, columns=self.columns, show="headings")
        for col in self.columns:
            tree.heading(col, text=col)
        for line in data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)
        # Insert tab
        self.frame_insert = ctk.CTkFrame(tab_insertion, fg_color="transparent")
        self.entries = []
        for i in range(len(self.columns)):
            # Row
            frame_row = ctk.CTkFrame(self.frame_insert)
            # Content
            label_insert = ctk.CTkLabel(frame_row, text=self.columns[i])
            entry_insert = ctk.CTkEntry(frame_row)
            self.entries.append(entry_insert)
            # Placement
            label_insert.grid(row=i, column=0, padx=15)
            entry_insert.grid(row=i, column=1, padx=15)
            frame_row.pack(pady=5)
        frame_row = ctk.CTkFrame(self.frame_insert)
        accept_button = ctk.CTkButton(frame_row, text="Accept", command=self.insert_data_into_db)
        accept_button.pack()
        frame_row.pack(pady=5)
        self.frame_insert.pack(pady=5)
        # Delete tab
        self.frame_delete = ctk.CTkFrame(tab_delete, fg_color="transparent")
        self.key_find = self.columns[0:2]
        frame_row = ctk.CTkFrame(self.frame_delete)
        label1_delete = ctk.CTkLabel(frame_row, text=self.key_find[0])
        self.entry1_delete = ctk.CTkEntry(frame_row)
        label1_delete.grid(row=i, column=0, padx=15)
        self.entry1_delete.grid(row=i, column=1, padx=15)
        frame_row.pack(pady=5)
        frame_row = ctk.CTkFrame(self.frame_delete)
        label2_delete = ctk.CTkLabel(frame_row, text=self.key_find[1])
        self.entry2_delete = ctk.CTkEntry(frame_row)
        label2_delete.grid(row=i, column=0, padx=15)
        self.entry2_delete.grid(row=i, column=1, padx=15)
        frame_row.pack(pady=5)
        frame_row = ctk.CTkFrame(self.frame_delete)
        delete_button = ctk.CTkButton(frame_row, text="Accept", command=self.delete_data_from_db_pair)
        delete_button.pack()
        frame_row.pack(pady=5)
        self.frame_delete.pack(pady=5)

    def draw_widgets(self) -> None:
        """Method to draw widgets 2"""
        self.set_style()
        # Tabs
        tab_control = ttk.Notebook(self.root)
        tab_table = ctk.CTkFrame(tab_control)
        tab_insertion = ctk.CTkFrame(tab_control)
        tab_delete = ctk.CTkFrame(tab_control)
        tab_control.add(tab_table, text="Table")
        tab_control.add(tab_insertion, text="Insert")
        tab_control.add(tab_delete, text="Delete")
        tab_control.pack(expand=1, fill="both")
        # Getting db data
        data = self.db_obj.get_table(self.title)
        self.columns = list(data[0].keys())
        # Db table
        tree = ttk.Treeview(master=tab_table, columns=self.columns, show="headings")
        for col in self.columns:
            tree.heading(col, text=col)
        for line in data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)
        # Insert tab
        self.frame_insert = ctk.CTkFrame(tab_insertion, fg_color="transparent")
        self.entries = []
        for i in range(len(self.columns)):
            # Row
            frame_row = ctk.CTkFrame(self.frame_insert)
            # Content
            label_insert = ctk.CTkLabel(frame_row, text=self.columns[i])
            entry_insert = ctk.CTkEntry(frame_row)
            self.entries.append(entry_insert)
            # Placement
            label_insert.grid(row=i, column=0, padx=15)
            entry_insert.grid(row=i, column=1, padx=15)
            frame_row.pack(pady=5)
        frame_row = ctk.CTkFrame(self.frame_insert)
        accept_button = ctk.CTkButton(frame_row, text="Accept", command=self.insert_data_into_db)
        accept_button.pack()
        frame_row.pack(pady=5)
        self.frame_insert.pack(pady=5)
        # Delete tab
        self.frame_delete = ctk.CTkFrame(tab_delete, fg_color="transparent")
        self.key_find = self.columns[0]
        frame_row = ctk.CTkFrame(self.frame_delete)
        label_delete = ctk.CTkLabel(frame_row, text=self.key_find)
        self.entry_delete = ctk.CTkEntry(frame_row)
        label_delete.grid(row=0, column=0, padx=15)
        self.entry_delete.grid(row=0, column=1, padx=15)
        frame_row.pack(pady=5)
        frame_row = ctk.CTkFrame(self.frame_delete)
        delete_button = ctk.CTkButton(frame_row, text="Accept", command=self.delete_data_from_db)
        delete_button.pack()
        frame_row.pack(pady=5)
        self.frame_delete.pack(pady=5)

    def grab_focus(self) -> None:
        """Making window running foreground"""
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
