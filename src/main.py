from moviepy import VideoFileClip
import signal; import sys
import random; import os

videos = ["benScott_excuses.mp4",
          "federer_perserverance.mp4",
          "forrestGump_destiny.mp4", 
          "goodWillHunting_potential.mp4",
          "jCole_procrastination.mp4",
          "kobe_failure.mp4",
          "kungFuPanda_identity.mp4",
          "science_curiosity.mp4",
          "various_changes.mp4",
          "whiplash_obsession.mp4"]

folder_path = "C:\Evan\engProjects\shortMotivations" 
path = os.path.join(folder_path, random.choice(videos))

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
    