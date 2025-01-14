#!/usr/bin/python3

import sys
import re
import os
import yaml
import click
from pathlib import Path

HERE = Path(__file__).parent.resolve()


@click.command(name="pop")
@click.argument("category")
@click.option(
    "--no-download",
    is_flag=True,
    show_default=True,
    default=False,
    help="Skip the download of a PDF.",
)
def main(category: str, no_download: bool):
    """
    Pops the first article of the reading list into read.

    """
    text = Path(f"{HERE}/../data/toread.md").read_text()

    with open(f"{HERE}/../data/config.yaml", "r") as c:
        shortcuts = yaml.load(c.read(), Loader=yaml.FullLoader)

    reading_list_code = category
    print(f'====== Pulling first QID in the "{shortcuts["lists"][reading_list_code]}" list ======')
    regex = shortcuts["lists"][reading_list_code] + r"[\s\S]*?(Q[0-9]*)"

    qid = re.findall(regex, text)[0]

    if qid == "Q":
        print("No QID found.")

    else:
        with open(f"{HERE}/../data/toread.md", "w+") as f:
            f.write(text.replace(qid + "\n", ""))
        if no_download:
            os.system(f"bib read {qid} --no-download")
        else:
            os.system(f"bib read {qid}")


if __name__ == "__main__":
    main()
