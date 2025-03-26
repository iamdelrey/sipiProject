"""File with MainWindow class"""
import customtkinter
import customtkinter as ctk
from .table_window import TableWindow
from .functions_window import FunctionsWindow
from PIL import Image


class MainWindow(ctk.CTk):
    """This class manages main window of application"""
    def __init__(self) -> None:
        """Constructor of class"""
        super().__init__()
        self.geometry("1080x400")
        self.resizable(False, False)
        self.title("db viewer")
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.draw_widgets()

    def open_computers(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "computers")

    def open_companies(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "service_companies")

    def open_plans(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "plans")

    def open_rooms(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "rooms")

    def open_types(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "computer_type")

    def open_components(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "components")

    def open_characteristics(self) -> None:
        """Method to open table"""
        window: TableWindow = TableWindow(self, "computer_characteristics")

    def open_functions(self) -> None:
        """Method to open table"""
        window: FunctionsWindow = FunctionsWindow(self, "functions")

    def draw_widgets(self) -> None:
        """Drawing all widgets on scheme"""
        # Main scheme
        # scheme_img = tkinter.PhotoImage(file="./assets/main.png")
        scheme_img = customtkinter.CTkImage(Image.open("./assets/main.png"), size=(1040, 315))
        scheme_label = ctk.CTkLabel(self, image=scheme_img, text="")
        scheme_label.pack(expand=1)
        # Computers button
        computers_button = ctk.CTkButton(
            self,
            text="Компьютеры",
            command=self.open_computers,
            height=7
        )
        computers_button.place(x=498, y=96)
        # Service companies button
        companies_button = ctk.CTkButton(
            self,
            text="Обслуживающие компании",
            command=self.open_companies,
            width=190,
            height=7
        )
        companies_button.place(x=473, y=223)
        # Plans button
        plans_button = ctk.CTkButton(
            self,
            text="Тарифы",
            command=self.open_plans,
            width=100,
            height=7
        )
        plans_button.place(x=927, y=174)
        # Rooms button
        rooms_button = ctk.CTkButton(
            self,
            text="Помещения",
            command=self.open_rooms,
            width=100,
            height=7
        )
        rooms_button.place(x=741, y=47)
        # Types button
        types_button = ctk.CTkButton(
            self,
            text="Типы компьютеров",
            command=self.open_types,
            width=100,
            height=7
        )
        types_button.place(x=730, y=161)
        # Components button
        components_button = ctk.CTkButton(
            self,
            text="Компоненты",
            command=self.open_components,
            width=120,
            height=7
        )
        components_button.place(x=56, y=143)
        # Characteristics button
        characteristics_button = ctk.CTkButton(
            self,
            text="Характеристики компьютеров",
            command=self.open_characteristics,
            width=120,
            height=7
        )
        characteristics_button.place(x=229, y=122)
        # Functions button
        # functions_image = tkinter.PhotoImage(file="./assets/fx.png")
        functions_image = customtkinter.CTkImage(Image.open("./assets/fx.png"), size=(15, 15))
        functions_button = ctk.CTkButton(
            self,
            text="",
            command=self.open_functions,
            width=1,
            height=1,
            image=functions_image
        )
        functions_button.place(x=1, y=1)
        author = ctk.CTkLabel(self, text="ⓒ Timothy")
        author.place(x=1010, y=375)

    def run_app(self) -> None:
        """Running an application"""
        self.mainloop()
