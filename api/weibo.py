import requests
import re

def parse_weibo(share_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        if "weibo.com" not in share_url:
            raise Exception("非微博链接")
        page_text = requests.get(share_url,headers=headers,timeout=10).text
        video_reg = re.compile(r'video_src":"(.*?)"')
        video_res = video_reg.findall(page_text)
        img_reg = re.compile(r'pic_id":"(.*?)"')
        img_res = img_reg.findall(page_text)
        video_url = video_res[0] if video_res else ""
        img_urls = [f"https://wx1.sinaimg.cn/large/{i}" for i in img_res]
        return {
            "title":"微博内容",
            "images":img_urls,
            "video":video_url
        }
    except Exception as e:
        raise Exception(f"微博解析失败：{str(e)}")
