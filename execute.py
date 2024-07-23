import os
import subprocess
import sys

def execute_commands(video_path):
    commands = [
        "pip install -r requirements.txt",
        f"python demo_script.py --in_video_path {video_path}"
    ]

    for command in commands:
        subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python execute_commands.py VIDEO_PATH")
        sys.exit(1)

    video_path = sys.argv[1]
    execute_commands(video_path)
