from moviepy import VideoFileClip
import random
import signal
import sys
import os




folder_path = r"C:\Evan\engProjects\shortMotivations\videos"
with os.scandir(folder_path) as videos:
    videos_list = list(videos)
    pick = random.randint(0, len(videos_list) - 1)
    video = videos_list[pick]
        
path = os.path.join(folder_path, video)

def safe_preview():
    clip = VideoFileClip(path)
    
    try:
        clip.preview(fps=clip.fps, audio=True)
    except (OSError, IOError, BrokenPipeError):
        pass
    finally:
        clip.close()
        sys.exit(0)

signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))

if __name__ == "__main__":
    safe_preview()
    