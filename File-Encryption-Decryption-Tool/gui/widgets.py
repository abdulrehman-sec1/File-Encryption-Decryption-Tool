"""
Custom UI functional abstraction elements.
"""
import customtkinter as ctk

class CustomLabel(ctk.CTkLabel):
    def __init__(self, master, text: str, font_size: int = 13, is_bold: bool = False, text_color: str = None, **kwargs):
        font_weight = "bold" if is_bold else "normal"
        super().__init__(
            master, 
            text=text, 
            font=ctk.CTkFont(family="Helvetica", size=font_size, weight=font_weight),
            text_color=text_color,
            **kwargs
        )