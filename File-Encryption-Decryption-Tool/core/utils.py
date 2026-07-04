"""
Helper system functions for human-readable outputs.
"""
import os

def get_readable_file_size(file_path: str) -> str:
    """Returns human-readable string values for file capacities."""
    if not os.path.exists(file_path):
        return "0 Bytes"
    size_bytes = os.path.getsize(file_path)
    for unit in ['Bytes', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"