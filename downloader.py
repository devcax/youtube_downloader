from requests import *
import pytube
import re
import math
import os
import yt_dlp as youtube_dl

def tumbnail(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    id = link.split('=')
    thumbnail_url = 'https://img.youtube.com/vi/' + id[1] + '/maxresdefault.jpg'

    thumbnail = get(thumbnail_url)
    with open(rf'{os.getcwd()}\cache\thumbnail.png', 'wb') as out_file:
        out_file.write(thumbnail.content)
    return thumbnail

def video_title(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    title = video.title
    return title

def video_views(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    views = video.views
    return views

def video_length(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    length = round(video.length/60 , 2)
    length = str(length)+' min'
    return length

def video_age(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    if video.age_restricted == True:
        age = "18+"
    else:
        age = 'No restrictions available'
    return age


def validator(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    x = re.search("^https://.*youtube.com.*watch", link)
    if x:
        return "Link accepted"
    elif re.search("^https://.", link) :
        return "Oops! i'm curiously struggling with your link 😤😤, \nBecause it is not a *youtube* link"
    else:
        return "Oops! I'm blind on your message, I think it is not a link ☹️☹️\nProbably it would be a text"


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})


def quality_sizemp3(link):
    args = link
    cnt = 1

    with ydl:
        result = ydl.extract_info(
            args,
            download=False  # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # if Just a video
        video = result

    size_listmp3 = []
    quality_listmp3 = []
    
    for k in video['formats']:
        if k['resolution'] == 'audio only':
            
            quality_listmp3.append(k['format_note'])
            if k['filesize'] != None:
                size_name = ("B", "KB", "MB", "GB", "TB")
                cal = int(math.floor(math.log(k['filesize'], 1024)))
                p = math.pow(1024, cal)
                s = round(k['filesize'] / p, 2)
                size_listmp3.append(f"{s} {size_name[cal]}")
            else:
                size_listmp3.append('null')
                      
            return size_listmp3,quality_listmp3
    

def quality_sizemp4(link):


    args = link
    cnt = 1

    with ydl:
        result = ydl.extract_info(
            args,
            download=False  # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # if Just a video
        video = result

    quality_list = []
    size_list = []
    height_list = []
   
            
    for i in video['formats']:
            if i['ext'] == 'mp4' and i['height'] not in height_list:
                if i['format_note'] == "DASH video":
                    quality_list.append(str(i['height'])+'p')
                else:
                    quality_list.append(i['format_note'])
                height_list.append(i['height'])
                try:
                    size = i['filesize']
                except:
                    size = 'none'
                if size != None:

                    size_name = ("B", "KB", "MB", "GB", "TB")
                    cal = int(math.floor(math.log(size, 1024)))
                    p = math.pow(1024, cal)
                    s = round(size / p, 2)
                    size_list.append(f"{s} {size_name[cal]}")
                else:
                    size_list.append('null')

    if '720p60' in quality_list:
        idx = quality_list.index('720p60')
        if '720p' in quality_list:
            quality_list.remove('720p60')
            size_list.pop(idx)
        else:
            quality_list[idx] = '720p'

    if '1080p60' in quality_list:
        idx = quality_list.index('1080p60')
        if '1080p' in quality_list:
            quality_list.remove('1080p60')
            size_list.pop(idx)
        else:
            quality_list[idx] = '1080p'
    if '1080p60' in quality_list:
        idx = quality_list.index('1080p60')
        if '1080p' in quality_list:
            quality_list.remove('1080p60')
            size_list.pop(idx)
        else:
            quality_list[idx] = '1080p'

    if '1440p60' in quality_list:
        idx = quality_list.index('1440p60')
        if '1080p' in quality_list:
            quality_list.remove('1440p60')
            size_list.pop(idx)
        else:
            quality_list[idx] = '1440p'

    if '2160p60' in quality_list:
        idx = quality_list.index('2160p60')
        if '1080p' in quality_list:
            quality_list.remove('2160p60')
            size_list.pop(idx)
        else:
            quality_list[idx] = '2160p'

    if '2160p60 HDR' in quality_list:
        idx = quality_list.index('2160p60 HDR')
        if '2160p' in quality_list:
            quality_list.remove('2160p60 HDR')
            size_list.pop(idx)
        else:
            quality_list[idx] = '2160p'

    if '1440p60 HDR' in quality_list:
        idx = quality_list.index('1440p60 HDR')
        if '1440p' in quality_list:
            quality_list.remove('1440p60 HDR')
            size_list.pop(idx)
        else:
            quality_list[idx] = '1440p'
    return quality_list,size_list

def download(link):
    ydl_options = {
    "progress_hooks": [callable_hook],
    }
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download([link])

def callable_hook(response):
    if response["status"] == "downloading":
        speed = response["speed"]
        print(speed)
        downloaded_percent = (response["downloaded_bytes"]*100)/response["total_bytes"]
        print('Speed',speed,'\n','Download precent',downloaded_percent)


