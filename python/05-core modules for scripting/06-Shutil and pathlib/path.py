from pathlib import Path
import subprocess

home = Path.home() / "Documents" / "secure.file"
print(home)
subprocess.run(["wl-copy" < home], shell=True)
