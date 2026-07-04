"""
Main application launch script wrapper.
"""
import sys
from gui.main_window import GuardVaultApp
from core.logger import app_logger

def main() -> None:
    try:
        app_logger.info("Initializing GuardVault Application Subsystem Layout Frameworks...")
        app = GuardVaultApp()
        app.mainloop()
        app_logger.info("Application execution runtime exited normally.")
    except Exception as e:
        app_logger.critical(f"Unhandled app startup crash condition: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()