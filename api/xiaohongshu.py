import requests
import re

def parse_xiaohongshu(share_url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
        "Cookie":"web_session=;"
    }
    try:
        if not ("xiaohongshu" in share_url or "xhslink" in share_url):
            raise Exception("非小红书链接")
        real_url = requests.get(share_url,headers=headers,allow_redirects=True,timeout=10).url
        note_id = re.search(r'note/(\d+)',real_url)
        if not note_id:
            raise Exception("提取笔记ID失败")
        nid = note_id.group(1)
        detail_api = f"https://www.xiaohongshu.com/api/sns/web/v1/feed?source=web_note_detail&note_id={nid}"
        json_res = requests.get(detail_api,headers=headers,timeout=10).json()
        item = json_res.get("data",{}).get("items",[])
        if not item:
            raise Exception("获取作品信息失败")
        info = item[0]
        video = info.get("video",{}).get("origin_video_url","")
        img_list = [i.get("url","") for i in info.get("image_list",[])]
        return {
            "title":info.get("title","小红书作品"),
            "content":info.get("desc",""),
            "images":img_list,
            "video":video
        }
    except Exception as e:
        raise Exception(f"小红书解析失败：{str(e)}")
