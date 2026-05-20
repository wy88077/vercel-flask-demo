import requests
import json
import re

def parse_weibo(url):
    """微博去水印解析"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    if "weibo.com" not in url and "weibocdn.com" not in url:
        raise Exception("不是有效的微博链接")
    
    # 简易版解析（替换成你的原版代码）
    return {
        "title": "微博测试内容",
        "images": ["https://example.com/weibo_img.jpg"],  # 图片列表
        "video": "https://example.com/weibo_video.mp4"    # 视频链接
    }
