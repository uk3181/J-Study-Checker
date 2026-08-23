from pathlib import Path
import os

DEBUG: bool = False

path: Path = Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'J-Study-Checker'

path.mkdir(parents=True, exist_ok=True)
