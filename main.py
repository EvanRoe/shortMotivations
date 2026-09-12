import subprocess
import random
import sys
import os

folder_path = r"C:\Evan\engProjects\shortMotivations\videos"

with os.scandir(folder_path) as videos:
    videos_list = list(videos)
    videos_dict = dict.fromkeys(videos_list, 0)
    count = 0

    if not os.path.exists("videos_counter.csv"):
        with open("videos_counter.csv", 'w') as file:
            lines = [f"{key}, {value}\n" for key, value in videos_dict.items()]
            file.writelines(lines)
    
    with open("videos_counter.csv", 'r') as file:
        for line in file:
            if line == file[0]:
                count == line
            pick = random.randint(0, len(videos_list) - 1)
            video = videos_list[pick]
        
path = os.path.join(folder_path, video)

subprocess.run(['ffplay', '-autoexit', '-fs', '-loglevel', 'quiet', path],
               shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
sys.exit(0)