import requests
import re

def parse_kuaishou(share_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        if not ("kuaishou" in share_url or "ks" in share_url):
            raise Exception("非快手链接")
        res = requests.get(share_url,headers=headers,allow_redirects=True,timeout=10)
        pattern = re.compile('shortVideo/(.*?)\?')
        result = pattern.findall(res.url)
        if not result:
            raise Exception("未找到视频ID")
        pid = result[0]
        api = f"https://www.kuaishou.com/short-video/{pid}"
        page = requests.get(api,headers=headers,timeout=10).text
        video_url = re.findall('src":"(.*?)","width',page)
        if not video_url:
            raise Exception("无水印地址获取失败")
        return {
            "title":"快手视频",
            "cover":"",
            "no_watermark_url":video_url[0]
        }
    except Exception as e:
        raise Exception(f"快手解析失败：{str(e)}")
