import requests
import re

def parse_douyin(share_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Referer":"https://www.douyin.com/"
    }
    try:
        if not ("douyin.com" in share_url or "dy" in share_url):
            raise Exception("非抖音链接")
        res = requests.get(share_url,headers=headers,allow_redirects=True,timeout=10)
        vid = re.findall(r'video/(\d+)',res.url)
        if not vid:
            raise Exception("提取视频ID失败")
        video_id = vid[0]
        api_url = f"https://www.iesdouyin.com/share/video/parse/link?url={share_url}"
        json_data = requests.get(api_url,headers=headers,timeout=10).json()
        if json_data.get("status") != 200:
            raise Exception("解析接口请求失败")
        data = json_data.get("data",{})
        return {
            "title":data.get("title","抖音视频"),
            "cover":data.get("cover",""),
            "no_watermark_url":data.get("nwm_video_url","")
        }
    except Exception as e:
        raise Exception(f"抖音解析失败：{str(e)}")
