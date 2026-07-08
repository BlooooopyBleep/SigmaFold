from dotenv import load_dotenv
import os
import subprocess

load_dotenv()

DIR = os.getenv('BASE_DIRECTORY')
PORT = os.getenv('PORT')
print(f"running SigmaFold from directory '{DIR}'")

subprocess.run(
    [
        f"python3",
        f"{DIR}website.py",
        f"--base_directory={DIR}",
        f"--port={PORT}"
    ]
)
