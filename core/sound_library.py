from pathlib import Path

SOUNDS_DIR = Path(__file__).parent.parent / "assets" / "sounds"

sounds = {}

for file in SOUNDS_DIR.iterdir():
    if file.is_file() and file.suffix.lower() in [".wav", ".mp3", ".m4a"]:
        sounds[file.stem] = str(file)

print(sounds)