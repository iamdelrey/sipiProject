"""File with FunctionsWindow class"""
import customtkinter
import customtkinter as ctk
import tkinter
from tkinter import ttk
from database.db import Database


class FunctionsWindow(ctk.CTk):
    """This class manages functions module in application"""
    def __init__(self, parent, title):
        """Constructor of class"""
        super().__init__()
        self.title = title
        self.db_obj = Database()
        self.root = ctk.CTkToplevel(parent)
        self.root.geometry("670x250")
        self.root.title(title)
        self.root.resizable(False, False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.draw_widgets()
        self.grab_focus()

    def get_comp_count(self) -> None:
        """Getting and drawing components count"""
        comp = self.entry_comp.get()
        comp_count = self.db_obj.call_comp_count(comp)
        count = list(comp_count[0].values())[0]
        self.comp_count_var.set(f"Количество: {count}")

    def get_plan_price(self) -> None:
        """Getting and drawing plan price"""
        plan = self.entry_price.get()
        active_data_price = self.db_obj.call_func_plan_price(plan)
        price = list(active_data_price[0].values())[0]
        self.result_var.set(f"Цена тарифа: {price}")

    def set_styles(self) -> None:
        """Setting styles for GUI"""
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
            tabposition="s"
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

    def draw_widgets(self) -> None:
        """Drawing all widgets on form"""
        # Styles exec
        self.set_styles()
        # Tabs
        tab_control = ttk.Notebook(self.root)
        tab_active_computers = ctk.CTkFrame(tab_control)
        tab_active_computers_count = ctk.CTkFrame(tab_control)
        tab_plan_price = ctk.CTkFrame(tab_control)
        tab_component_count = ctk.CTkFrame(tab_control)
        tab_control.add(tab_active_computers, text="Включенные компьютеры")
        tab_control.add(tab_active_computers_count, text="Количество включенных компьютеров")
        tab_control.add(tab_plan_price, text="Получить цену тарифа")
        tab_control.add(tab_component_count, text="Количество комплектующих")
        tab_control.pack(expand=1, fill="both")
        # Active computers count
        active_count_data = self.db_obj.call_proc_active_count()
        active_count_data_keys = list(active_count_data[0].keys())
        tree = ttk.Treeview(master=tab_active_computers_count, columns=active_count_data_keys, show="headings")
        for col in active_count_data_keys:
            tree.heading(col, text=col)
        for line in active_count_data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)
        # Active computers
        active_data = self.db_obj.call_proc_active()
        active_data_keys = list(active_data[0].keys())
        tree = ttk.Treeview(master=tab_active_computers, columns=active_data_keys, show="headings")
        for col in active_data_keys:
            tree.heading(col, text=col)
        for line in active_data:
            tree.insert("", tkinter.END, values=list(line.values()), tags=("odd",))
        tree.pack(fill=tkinter.BOTH, expand=1)
        # Active plans price
        plan_price_frame = ctk.CTkFrame(tab_plan_price, fg_color="transparent")
        # Result label
        self.result_var = tkinter.StringVar()
        price_result_lbl = ctk.CTkLabel(plan_price_frame, textvariable=self.result_var)
        price_result_lbl.pack(pady=10)
        # Row
        row_func_price = ctk.CTkFrame(plan_price_frame)
        label_price = ctk.CTkLabel(row_func_price, text="Тариф")
        self.entry_price = ctk.CTkEntry(row_func_price)
        label_price.grid(row=0, column=0, padx=15)
        self.entry_price.grid(row=0, column=1, padx=15)
        row_func_price.pack(pady=5)
        # Button
        price_btn = ctk.CTkButton(plan_price_frame, text="Accept", command=self.get_plan_price)
        price_btn.pack(pady=5)
        plan_price_frame.pack()
        # Comp count
        comp_count_frame = ctk.CTkFrame(tab_component_count, fg_color="transparent")
        # Result label
        self.comp_count_var = tkinter.StringVar()
        comp_lbl = ctk.CTkLabel(comp_count_frame, textvariable=self.comp_count_var)
        comp_lbl.pack(pady=10)
        # Row
        row_comp = ctk.CTkFrame(comp_count_frame)
        label_comp = ctk.CTkLabel(row_comp, text="Комплектующее")
        self.entry_comp = ctk.CTkEntry(row_comp)
        label_comp.grid(row=0, column=0, padx=15)
        self.entry_comp.grid(row=0, column=1, padx=15)
        row_comp.pack(pady=5)
        # Button
        comp_btn = ctk.CTkButton(comp_count_frame, text="Accept", command=self.get_comp_count)
        comp_btn.pack(pady=5)
        comp_count_frame.pack()

    def grab_focus(self) -> None:
        """Making window running foreground"""
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
