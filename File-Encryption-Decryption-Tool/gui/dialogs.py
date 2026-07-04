"""
Alert UI abstraction layers using Tkinter messageboxes safely.
"""
from tkinter import messagebox

class DialogManager:
    
    @staticmethod
    def show_info(title: str, message: str) -> None:
        messagebox.showinfo(title, message)
        
    @staticmethod
    def show_error(title: str, message: str) -> None:
        messagebox.showerror(title, message)
        
    @staticmethod
    def show_warning(title: str, message: str) -> None:
        messagebox.showwarning(title, message)