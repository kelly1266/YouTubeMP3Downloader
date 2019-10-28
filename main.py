from __future__ import unicode_literals
import youtube_dl
from pydub import AudioSegment
#from pydub import AudioSegment


def run_downloader(parent_dir, url, name):

    filepath =parent_dir+ '/' + str(name) + '.%(ext)s'
    ydl_opts = {
        'outtmpl': filepath,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print('Download complete')


parent_dir = input('Enter the parent directory you would like your files to be saved to: ')
url = input('Enter youtube url (remember to add a space before you hit return): ')
name = input('Enter desired file name: ')
run_downloader(parent_dir, url, name)
trim_clip=input('Do you want to edit the start/end time of this audio clip? y/n: ')
if trim_clip == 'y' or trim_clip == 'Y':
    file_name=parent_dir+'\\'+name
    audio=AudioSegment.from_mp3(file_name+'.mp3')
    start_time=int(input('Enter start time in seconds: '))
    start_time*=1000
    end_time=int(input('Enter end time in seconds: '))
    end_time*=1000
    extract=audio[start_time:end_time]
    extract.export(file_name+'-extract.mp3', format='mp3')
