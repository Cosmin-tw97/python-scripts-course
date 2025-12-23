import functools
from datetime import datetime

def log_task_completion(func):
    """Decorator that logs when a task is finished."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Task processed successfully.")
        return result
    return wrapper