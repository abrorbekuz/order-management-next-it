import threading
import logging

logger = logging.getLogger(__name__)

def run_silent(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=_safe_run, args=(func, args, kwargs))
        thread.setDaemon(True)
        thread.start()

    return wrapper

def _safe_run(func, args, kwargs):
    try:
        func(*args, **kwargs)
    except Exception as e:
        logger.exception(f"Async function {func.__name__} failed: {e}")
