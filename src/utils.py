from pathlib import Path


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def print_section(title):
    print(f"\n{'='*50}")
    print(title)
    print(f"{'='*50}")
