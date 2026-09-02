#!/usr/bin/env python3
"""
Kaggle Notebook Metadata — kaggle.json
This file tells Kaggle how to run your notebook.

Place this file in your GitHub repo root.
The GitHub Actions workflow uses it when running `kaggle kernels push`.

Already configured for username: djoshi7
"""

import json

KAGGLE_METADATA = {
    "id": "djoshi7/wzml-x",
    "id_no": "djoshi7_wzml_x",
    "title": "wzml-x",
    "code_file": "kaggle_notebook.py",
    "language": "python",
    "kernel_type": "script",
    "is_private": "true",
    "enable_gpu": "false",
    "enable_tpu": "false",
    "enable_internet": "true",
    "dataset_sources": [
        "djoshi7/wzmlx-config"
    ],
    "competition_sources": [],
    "kernel_sources": [],
    "model_sources": []
}

if __name__ == "__main__":
    with open("kaggle.json", "w") as f:
        json.dump(KAGGLE_METADATA, f, indent=2)
    print("kaggle.json created for user: djoshi7")
    print("\nContents:")
    print(json.dumps(KAGGLE_METADATA, indent=2))

