import requests
import json
import re
from bs4 import BeautifulSoup

def parse_xiaohongshu(url):
    """小红书去水印解析"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    if "xiaohongshu.com" not in url and "xhslink.com" not in url:
        raise Exception("不是有效的小红书链接")
    
    # 简易版解析（替换成你的原版代码）
    return {
        "title": "小红书测试笔记",
        "content": "测试内容",
        "images": ["https://example.com/img1.jpg"],  # 图片列表
        "video": "https://example.com/xhs_video.mp4"  # 视频链接（无则为""）
    }
