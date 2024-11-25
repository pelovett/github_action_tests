import sys


def check_for_changed_files(filepath: str):
    print(f"Running with path: {filepath}")

if __name__ == "__main__":
    check_for_changed_files(sys.argv[1])