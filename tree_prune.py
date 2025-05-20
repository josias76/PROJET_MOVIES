import os

EXCLUDE_PATTERNS = ['build', '__pycache__']
EXCLUDE_SUFFIXES = ['.egg-info']

def is_excluded(name):
    if name in EXCLUDE_PATTERNS:
        return True
    for suffix in EXCLUDE_SUFFIXES:
        if name.endswith(suffix):
            return True
    return False

def tree(dir_path, prefix=''):
    entries = []
    for name in sorted(os.listdir(dir_path)):
        if is_excluded(name):
            continue
        entries.append(name)

    # Prune: ne pas afficher le dossier s'il est vide après exclusion
    if not entries:
        return

    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            tree(path, prefix + extension)

if __name__ == "__main__":
    import sys
    start_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(start_path)
    tree(start_path)
