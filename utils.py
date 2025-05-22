def ensure_dir(path):
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True)
