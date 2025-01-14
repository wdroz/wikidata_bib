#!/usr/bin/python3

import sys
from helper import download_paper, get_doi_df
from pathlib import Path
import webbrowser

HERE = Path(__file__).parent.resolve()


def main():
    wikidata_id = sys.argv[1]
    source = sys.argv[2]
    doi_df = get_doi_df(wikidata_id)
    print("======= Looking for article DOI on Wikidata =======")
    print(doi_df)
    if doi_df.empty == True:
        print("No DOI found for " + wikidata_id + ".")

    else:
        doi_suffix = doi_df["doi"].values[0]
        webbrowser.open(f"https://doi.org/{doi_suffix}")
        print("DOI: " + doi_suffix)
        download_paper(doi=doi_suffix, source=source, path=f"{HERE}/../../downloads/")


if __name__ == "__main__":
    main()
