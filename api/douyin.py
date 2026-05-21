from flask import Blueprint, request, jsonify
import requests
import re

douyin = Blueprint('douyin', __name__)

@douyin.route('/api/douyin', methods=['GET'])
def parse_douyin():
    try:
        # 获取前端传的抖音链接
        url = request.args.get('url')
        if not url:
            return jsonify({'code': -1, 'msg': '请传入抖音链接'})
        
        # 第一步：解析抖音短链接，获取真实链接
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        # 处理抖音口令/短链接
        if '复制打开抖音' in url:
            # 提取短链接
            short_url = re.findall(r'https?://\S+', url)[0]
        else:
            short_url = url
        
        # 请求短链接，获取真实地址
        res = requests.get(short_url, headers=headers, allow_redirects=False)
        real_url = res.headers.get('Location', short_url)
        
        # 第二步：调用解析接口获取无水印链接（通用接口，稳定）
        parse_res = requests.get(f'https://api.vvhan.com/api/douyin?url={real_url}', headers=headers)
        if parse_res.status_code == 200:
            data = parse_res.json()
            if data.get('success') and data.get('data').get('play'):
                return jsonify({
                    'code': 200,
                    'msg': '解析成功',
                    'data': {
                        'url': data['data']['play']
                    }
                })
            else:
                return jsonify({'code': -1, 'msg': '解析失败，无视频链接'})
        else:
            return jsonify({'code': -1, 'msg': '解析接口请求失败'})
    except Exception as e:
        return jsonify({'code': -1, 'msg': f'解析出错：{str(e)}'})

# 如果是app.py主文件，添加下面的注册代码
# from flask import Flask
# app = Flask(__name__)
# app.register_blueprint(douyin)
