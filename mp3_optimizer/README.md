# optimize. compress your MP3 files. 
This Python code takes the input and output paths, then compresses the .mp3 files in the input folder to a frame rate of 32000 Hz and places the compressed .mp3 file in the output folder. 
(The files that cannot be converted for some reason are copied exactly to the output folder) and finally it displays the amount of reduced volume.


## Usage:
### A- install requirements packages:
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


### B- download mp3_optimizer.py and edit these lines code: (Determining the path of the input and output folders)
input_directory = 'X:/your-music-folder-path'
output_directory = 'X:/your-compressed-folder-path' #The path of the folder where you want the compressed music to be placed.

#For more compression, change all frame rate numbers from 32000 to 11025. (The quality will decrease slightly)

### C- run it


