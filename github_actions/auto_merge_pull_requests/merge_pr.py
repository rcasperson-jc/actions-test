#!/usr/bin/env python
import sys
import os

if __name__ == "__main__":
    print("Hello world!")
    print(os.environ["GITHUB_TOKEN"])
    sys.exit(1)
