import os
import sys
from typing import List


def check_for_changed_files(filepaths: List[str]):
    warnings = []
    print(f"Running with paths: {filepaths}")
    if "a/b.txt" in filepaths and "a/c.txt" not in filepaths:
        warnings.append("If you're changing a/b.txt make sure to also update a/c.txt !")

    with open(os.environ["GITHUB_OUTPUT"], 'a') as output_buf:
        warnings_str = '\n'.join(warnings)
        output_buf.write(f"warnings={warnings_str}")


if __name__ == "__main__":
    check_for_changed_files(sys.argv[1:])