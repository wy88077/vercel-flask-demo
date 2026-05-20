import requests
import json
import re

def parse_kuaishou(url):
    """快手去水印解析"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    if "kuaishou.com" not in url and "ksweb.link" not in url:
        raise Exception("不是有效的快手链接")
    
    # 简易版解析（替换成你的原版代码）
    return {
        "title": "快手测试视频",
        "cover": "https://example.com/cover.jpg",
        "no_watermark_url": "https://example.com/kuaishou_video.mp4"
    }
