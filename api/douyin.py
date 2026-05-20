import requests
import json

def parse_douyin(url):
    """抖音去水印解析"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.douyin.com/"
    }
    
    if "douyin.com" not in url and "dycdn.net" not in url:
        raise Exception("不是有效的抖音链接")
    
    # 简易版解析（替换成你的原版代码）
    return {
        "title": "抖音测试视频",
        "cover": "https://example.com/cover.jpg",
        "no_watermark_url": "https://example.com/douyin_video.mp4"
    }
