""" This is main file. This file executes the application
"""
from windows.main_window import MainWindow


def main() -> None:
    """Main function to run an application"""
    app: MainWindow = MainWindow()
    app.run_app()


if __name__ == "__main__":
    main()
