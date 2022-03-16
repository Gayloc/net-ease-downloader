import requests
import json
import eyed3
import asyncio
from eyed3.id3.frames import ImageFrame
import os
import re
import sys

url_api='https://netease-cloud-music-api-six-rouge.vercel.app/song/detail?ids={}'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
     'Referer':'http://music.163.com/'
    }
if len(sys.argv)==1:
    song_id=input("输入id\n")
if len(sys.argv)==2:
    song_id=sys.argv[1]
url=url_api.format(song_id) #合成信息链接

#获取音乐信息
print("获取音乐信息")
details=requests.get(url).text
dict_details=json.loads(details)
song=dict_details['songs']
song_name=song[0]['name']   #歌曲的名字
song_ar=song[0]['ar'][0]['name']
song_al=song[0]['al']['name']
picurl=song[0]['al']['picUrl']

#下载音乐本体
print("下载音乐")
url_download='http://music.163.com/song/media/outer/url?id={}.mp3'  #临时用的链接
url_d=url_download.format(song_id)  #合成下载链接
song_main=requests.get(url_d,headers=headers).content
name=song_name+".mp3"   #带后缀名的歌曲名
with open(name,'wb') as f:
    f.write(song_main)
    
#下载歌曲封面
print("下载歌曲封面")
pic=requests.get(picurl,headers=headers).content
pic_name="cover.jpg"
with open(pic_name,'wb') as f:
    f.write(pic)

#下载歌词
print("下载歌词")
lyric_original_url="https://netease-cloud-music-api-six-rouge.vercel.app/lyric?id={}"
lyric_url=lyric_original_url.format(song_id)
lyric_original=requests.get(lyric_url).text
lyric=json.loads(lyric_original)['lrc']['lyric']

#将歌曲与信息整合
print("信息整合")
audiofile=eyed3.load(name)
audiofile.tag.artist=song_ar
audiofile.tag.title=song_name
audiofile.tag.album=song_al
audiofile.tag.lyrics.set=lyric
audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(pic_name,'rb').read(), 'image/jpeg')
audiofile.tag.save()
print("完成")
#清理临时文件
os.remove(pic_name)
