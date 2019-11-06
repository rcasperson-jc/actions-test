#!/usr/bin/env python
import sys
import os

import requests


def create_session(github_token):
    sess = requests.Session()
    sess.headers = {
        "Accept": "; ".join([
            "application/vnd.github.v3+json",
            "application/vnd.github.antiope-preview+json",
        ]),
        "Authorization": f"token {github_token}",
        "User-Agent": f"GitHub Actions script in {__file__}"
    }

    def raise_for_status(resp, *args, **kwargs):
        try:
            resp.raise_for_status()
        except Exception:
            print(resp.text)
            sys.exit("Error: Invalid repo, token or network issue!")

    sess.hooks["response"].append(raise_for_status)
    return sess

if __name__ == "__main__":
    print("Hello world!")
    sess = create_session(os.environ["GITHUB_TOKEN"])
