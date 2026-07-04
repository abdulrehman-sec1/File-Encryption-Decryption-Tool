"""
Main window modern desktop graphical layout.
"""
import os
import threading
import customtkinter as ctk
from tkinter import filedialog

import config
from core.validator import Validator
from core.encryption import FileEncryptor
from core.decryption import FileDecryptor
from core.utils import get_readable_file_size
from core.logger import app_logger

from gui.widgets import CustomLabel
from gui.dialogs import DialogManager
import gui.theme as theme

class GuardVaultApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.selected_file_path: str = ""
        
        # Configure Main Window
        self.title(config.WINDOW_TITLE)
        self.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.resizable(False, False)
        
        ctk.set_appearance_mode(config.THEME_MODE)
        ctk.set_default_color_theme(config.COLOR_THEME)
        
        self.build_ui()
        
    def build_ui(self) -> None:
        # Top Header Container Layout
        self.header_frame = ctk.CTkFrame(self, corner_radius=0, height=70)
        self.header_frame.pack(fill="x", side="top")
        
        self.title_label = CustomLabel(self.header_frame, text="🔒 GuardVault File Crypto Engine", font_size=20, is_bold=True)
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Main Layout Form Element Fields
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=30, pady=20)
        
        # File Choice Picker Widget Layer
        self.file_btn = ctk.CTkButton(self.main_container, text="Select Target File", command=self.handle_file_selection, height=38, font=ctk.CTkFont(weight="bold"))
        self.file_btn.pack(fill="x", pady=(10, 5))
        
        self.file_status_label = CustomLabel(self.main_container, text="No active file loaded.", text_color=theme.TEXT_MUTED)
        self.file_status_label.pack(fill="x", pady=(0, 15))
        
        # Passphrase Entry Fields
        self.pass_label = CustomLabel(self.main_container, text="Master Security Passphrase", is_bold=True)
        self.pass_label.pack(anchor="w")
        
        self.pass_entry = ctk.CTkEntry(self.main_container, show="*", placeholder_text="Enter secure key phrase", height=36)
        self.pass_entry.pack(fill="x", pady=(5, 12))
        self.pass_entry.bind("<KeyRelease>", self.evaluate_password_complexity)
        
        self.confirm_pass_label = CustomLabel(self.main_container, text="Confirm Master Passphrase (Required for Encryption)", is_bold=True)
        self.confirm_pass_label.pack(anchor="w")
        
        self.confirm_pass_entry = ctk.CTkEntry(self.main_container, show="*", placeholder_text="Confirm key phrase details", height=36)
        self.confirm_pass_entry.pack(fill="x", pady=(5, 5))
        
        # Live Password Metrics Subsystem
        self.strength_bar = ctk.CTkProgressBar(self.main_container, height=6)
        self.strength_bar.pack(fill="x", pady=(5, 2))
        self.strength_bar.set(0)
        
        self.strength_label = CustomLabel(self.main_container, text="Password Strength: Not Evaluated", font_size=11, text_color=theme.TEXT_MUTED)
        self.strength_label.pack(anchor="w", pady=(0, 20))
        
        # Execution Call Actions Frame Assembly
        self.action_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.action_frame.pack(fill="x", pady=10)
        
        self.encrypt_btn = ctk.CTkButton(self.action_frame, text="Encrypt File", fg_color=theme.ACCENT_GREEN, hover_color="#248437", command=self.trigger_encryption, height=42, font=ctk.CTkFont(weight="bold"))
        self.encrypt_btn.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        self.decrypt_btn = ctk.CTkButton(self.action_frame, text="Decrypt File", fg_color="#1F6AA5", hover_color="#144870", command=self.trigger_decryption, height=42, font=ctk.CTkFont(weight="bold"))
        self.decrypt_btn.pack(side="right", expand=True, fill="x", padx=(10, 0))
        
        # Global Operational Status and Metrics
        self.progress_bar = ctk.CTkProgressBar(self.main_container, height=10)
        self.progress_bar.pack(fill="x", pady=(20, 5))
        self.progress_bar.set(0)
        
        self.global_status_label = CustomLabel(self.main_container, text="System Idle", font_size=13, is_bold=True)
        self.global_status_label.pack(anchor="center")
        
        # App Footer Section
        self.footer_label = CustomLabel(self, text="AES-256-GCM Production Engine Layer • Secure Core", font_size=10, text_color=theme.TEXT_MUTED)
        self.footer_label.pack(side="bottom", pady=8)

    def handle_file_selection(self) -> None:
        selected = filedialog.askopenfilename(title="Select File for Transformation Ops")
        if selected:
            self.selected_file_path = selected
            size_str = get_readable_file_size(selected)
            self.file_status_label.configure(text=f"Loaded: {os.path.basename(selected)} ({size_str})", text_color="#FFFFFF")
            app_logger.info(f"UI referenced target file successfully: {selected}")

    def evaluate_password_complexity(self, event=None) -> None:
        pwd = self.pass_entry.get()
        if not pwd:
            self.strength_bar.set(0)
            self.strength_label.configure(text="Password Strength: Not Evaluated", text_color=theme.TEXT_MUTED)
            return
            
        score, desc = Validator.check_password_strength(pwd)
        self.strength_bar.set(score / 4.0)
        
        if score <= 1:
            self.strength_bar.configure(progress_color=theme.ACCENT_RED)
            self.strength_label.configure(text=f"Password Strength: {desc}", text_color=theme.ACCENT_RED)
        elif score <= 3:
            self.strength_bar.configure(progress_color="#E6A23C")
            self.strength_label.configure(text=f"Password Strength: {desc}", text_color="#E6A23C")
        else:
            self.strength_bar.configure(progress_color=theme.ACCENT_GREEN)
            self.strength_label.configure(text=f"Password Strength: {desc}", text_color=theme.ACCENT_GREEN)

    def set_ui_state(self, enabled: bool) -> None:
        state = "normal" if enabled else "disabled"
        self.file_btn.configure(state=state)
        self.encrypt_btn.configure(state=state)
        self.decrypt_btn.configure(state=state)

    def update_progress(self, val: float) -> None:
        self.progress_bar.set(val)
        self.update_idletasks()

    def trigger_encryption(self) -> None:
        # Validate Input Values and Passphrases
        valid, err = Validator.validate_file_for_encryption(self.selected_file_path)
        if not valid:
            DialogManager.show_error("Validation Failure", err)
            return
            
        pwd = self.pass_entry.get()
        confirm_pwd = self.confirm_pass_entry.get()
        
        if not pwd:
            DialogManager.show_error("Input Required", "Symmetric key string cannot be empty.")
            return
        if pwd != confirm_pwd:
            DialogManager.show_error("Mismatch Error", "Passphrase confirmation entries do not match.")
            return
            
        self.set_ui_state(False)
        self.global_status_label.configure(text="Encrypting file asset contents...", text_color="#E6A23C")
        
        def run():
            try:
                out_path = FileEncryptor.encrypt_file(self.selected_file_path, pwd, self.update_progress)
                self.global_status_label.configure(text="Encryption finished successfully.", text_color=theme.ACCENT_GREEN)
                DialogManager.show_info("Operation Successful", f"File safely processed. Saved to:\n{out_path}")
            except Exception as e:
                app_logger.exception("Unexpected structural crash during execution flow processing.")
                self.global_status_label.configure(text="Operation failed.", text_color=theme.ACCENT_RED)
                DialogManager.show_error("Internal Execution Error", f"Fatal runtime event: {str(e)}")
            finally:
                self.set_ui_state(True)
                
        threading.Thread(target=run, daemon=True).start()

    def trigger_decryption(self) -> None:
        valid, err = Validator.validate_file_for_decryption(self.selected_file_path, config.ENCRYPTED_FILE_EXTENSION)
        if not valid:
            DialogManager.show_error("Validation Failure", err)
            return
            
        pwd = self.pass_entry.get()
        if not pwd:
            DialogManager.show_error("Input Required", "You must provide a decryption passkey sequence.")
            return
            
        self.set_ui_state(False)
        self.global_status_label.configure(text="Decrypting and verifying signatures...", text_color="#E6A23C")
        
        def run():
            try:
                out_path = FileDecryptor.decrypt_file(self.selected_file_path, pwd, self.update_progress)
                self.global_status_label.configure(text="Decryption verified and completed.", text_color=theme.ACCENT_GREEN)
                DialogManager.show_info("Operation Successful", f"Asset contents successfully decrypted:\n{out_path}")
            except PermissionError as pe:
                self.global_status_label.configure(text="Authentication verification failed.", text_color=theme.ACCENT_RED)
                DialogManager.show_error("Authentication Denied", "Incorrect password or payload modification detected.")
            except Exception as e:
                app_logger.exception("Unexpected error inside critical decrypt execution pathways.")
                self.global_status_label.configure(text="Operation failed.", text_color=theme.ACCENT_RED)
                DialogManager.show_error("Internal System Error", f"Fatal decryption execution event: {str(e)}")
            finally:
                self.set_ui_state(True)
                
        threading.Thread(target=run, daemon=True).start()