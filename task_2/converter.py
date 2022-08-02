import urllib.request
from moviepy.editor import VideoFileClip
import os


video_url = "https://v16m-webapp.tiktokcdn-us.com/a6e3b7e6a064bc43da3a39ab93460ef8/62e921d5/video/tos/useast5/tos-useast5-ve-0068c003-tx/41b44c2a3cc840929f658665d57979d1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=1150&bt=575&cs=0&ds=3&ft=ebtHKH-qMyq8ZwkJKwe2NoTcfl7Gb&mime_type=video_mp4&qs=0&rc=aTozOTNmZmg5MzpnOzo1ZUBpM3g6OmQ6ZmhvZTMzZzczNEAwLjRiMDZhNmMxLmJfMTYzYSNqczAycjRnYmZgLS1kMS9zcw%3D%3D&l=20220802070706CBA8CD072C869B2562D9"


def converter(video_url):
    video_mp4 = urllib.request.urlretrieve(video_url, "test.mp4")
    video_path = video_mp4[0]
    video = VideoFileClip(video_path)
    video_to_gif = video.write_gif("test.gif")
    gif_path = os.path.abspath("test.gif")
    return print(f"This is the path to gif: {gif_path}")


converter(video_url)




