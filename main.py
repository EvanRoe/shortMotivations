import subprocess
import random
import sys
import os

folder_path = r"C:\Evan\engProjects\shortMotivations\videos"
with os.scandir(folder_path) as videos:
    videos_list = list(videos)
    pick = random.randint(0, len(videos_list) - 1)
    video = videos_list[pick]
        
path = os.path.join(folder_path, video)

subprocess.run(['ffplay', '-autoexit', '-fs', '-loglevel', 'quiet', path],
               shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.exit(0)