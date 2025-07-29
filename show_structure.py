import os

def print_structure(root_dir, prefix=""):
    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        print(prefix + "├── " + item)
        if os.path.isdir(path):
            print_structure(path, prefix + "│   ")

if __name__ == "__main__":
    print("Struktur folder:")
    print_structure(".")
