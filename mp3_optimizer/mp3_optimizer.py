#!/usr/bin/env python
"""
Compress mp3 files to frame rate 32000 to reduce file size.
I optimized and improved the codes in link https://github.com/easy4u/mp3c/.

Requirements to run the script:
1. pydub
$ pip install pydu

2. ffmpeg (linux)
$ brew install ffmpeg --with-libvorbis --with-ffplay --with-theora

2. ffmpeg (windows)
In Windows PowerShell, the commands should be executed as follows:

1. Installing Chocolatey:
>>> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

2. Install ffmpeg:
>>> choco install ffmpeg


Do you want to run the script? ([Y]es/[A]ll - yes to all/[N]o/[P]rint): plz type A

More tips: Open it by searching for "PowerShell" in the Windows Start menu. Please note that you need administrator access to run these commands. To do this, right-click on the PowerShell icon
and select "Run as Administrator". After opening PowerShell with administrator access, copy and paste above commands there and run. 
These commands install Chocolatey (a package manager for Windows) and then install ffmpeg using Chocolatey.
"""

import os
import shutil
from pydub import AudioSegment

# Determining the path of the input and output folders
input_directory = 'X:/your-music-folder-path'
output_directory = 'X:/your-compressed-folder-path' #The path of the folder where you want the compressed music to be placed.

def get_folder_size(folder_path):
    total = 0
    for path, dirs, files in os.walk(folder_path):
        for f in files:
            fp = os.path.join(path, f)
            total += os.path.getsize(fp)
    return total

def compress_mp3_file(mp3_file_path, output_directory):
    if (not mp3_file_path.endswith(".mp3")): return

    output_file_path = os.path.join(output_directory, os.path.basename(mp3_file_path))
    print("\n Processing {} ==> {}".format(mp3_file_path, output_file_path))

    try:
        audio_file = AudioSegment.from_file(mp3_file_path, "mp3")
        frame_rate = audio_file.frame_rate

        if (frame_rate == 32000):
            print (" frame rate is already 32000, ignore.")
            return

        print(" frame_rate {} ==> {}".format(frame_rate, "32000"))
        audio_file.export(output_file_path, format="mp3", parameters=["-ar", "32000"]) #more compress: 11025
    except Exception as e:
        print(" Error processing file: {}. Copying original file to output directory.".format(e))
        shutil.copy(mp3_file_path, output_file_path)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

mp3_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith(".mp3")]

print("\n Files to process: {}".format(mp3_files))

initial_size = get_folder_size(input_directory)

for mp3_file in mp3_files:
    compress_mp3_file(mp3_file, output_directory)

final_size = get_folder_size(output_directory)
reduction = initial_size - final_size

print ("\n DONE. Reduced the folder size by {:.2f} MB.".format(reduction / 1048576))
