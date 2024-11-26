import os
import sys
from typing import List


def check_for_changed_files(filepaths: List[str]):
    warnings = []
    print(f"Running with paths: {filepaths}")
    if "a/b.txt" in filepaths and "a/c.txt" not in filepaths:
        print(f"User has edited a/b.txt but not a/c.txt")
        warnings.append(
            "If you're changing\n\`\`\`\n/arion/arion-kraken/scripts/etl/kraken_traffic/rebuild/gen_rebuild_reph_kraken_traffic.sql\n\`\`\`\nmake sure to also update\n\`\`\`\n/arion/arion-kraken/scripts/etl/kraken_traffic/gen_reph_kraken_traffic.sqls\n\`\`\`"
        )

    with open(os.environ["GITHUB_OUTPUT"], "a") as output_buf:
        warnings_str = "\n".join(warnings)
        output_buf.write(f"warnings<<EOF\n{warnings_str}\nEOF\n")

    with open(os.environ["GITHUB_OUTPUT"], "a") as output_buf:
        warnings_str = "\n".join(warnings)
        output_buf.write(f"should_comment=true")


if __name__ == "__main__":
    check_for_changed_files(sys.argv[1:])
