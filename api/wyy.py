import requests
from urllib.parse import urlparse, parse_qs

def parse_wyy(share_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        if "music.163.com" not in share_url:
            raise Exception("非网易云音乐链接")
        res = requests.get(share_url,headers=headers,timeout=10)
        song_id = ""
        if "song?id=" in res.url:
            song_id = res.url.split("id=")[-1].split("&")[0]
        if not song_id:
            raise Exception("获取歌曲ID失败")
        api = f"https://music.163.com/song/media/outer/url?id={song_id}.mp3"
        return {
            "title":"网易云音乐",
            "author":"",
            "no_watermark_url":api
        }
    except Exception as e:
        raise Exception(str(e))
