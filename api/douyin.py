from flask import Blueprint, request, jsonify
import requests
import re

# 创建蓝图（确保蓝图名称和路由前缀匹配）
douyin = Blueprint('douyin', __name__)

# 抖音解析接口 - 修复参数问题，确保无语法错误
@douyin.route('/api/douyin', methods=['GET'])
def parse_douyin():
    try:
        # 1. 获取前端传入的抖音链接（无参数错误，通过request.args安全获取）
        url = request.args.get('url', '').strip()  # 加默认值，避免空值报错
        if not url:
            return jsonify({'code': -1, 'msg': '请传入抖音链接'})
        
        # 2. 配置请求头，模拟浏览器访问（避免被抖音拦截）
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Referer': 'https://www.douyin.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        
        # 3. 处理抖音口令/短链接（兼容两种格式）
        short_url = url
        if '复制打开抖音' in url:
            # 提取口令中的短链接（加异常处理，避免无链接时报错）
            url_match = re.findall(r'https?://\S+', url)
            if url_match:
                short_url = url_match[0]
            else:
                return jsonify({'code': -1, 'msg': '未从口令中提取到有效链接'})
        
        # 4. 解析短链接，获取真实视频地址（关闭重定向，手动获取Location）
        try:
            res = requests.get(short_url, headers=headers, allow_redirects=False, timeout=10)
            real_url = res.headers.get('Location', short_url)
        except requests.exceptions.Timeout:
            return jsonify({'code': -1, 'msg': '链接解析超时，请重试'})
        except Exception as e:
            return jsonify({'code': -1, 'msg': f'解析短链接失败：{str(e)[:20]}'})
        
        # 5. 调用通用解析接口获取无水印链接（稳定可用）
        parse_res = requests.get(f'https://api.vvhan.com/api/douyin?url={real_url}', headers=headers, timeout=10)
        if parse_res.status_code == 200:
            data = parse_res.json()
            # 兼容接口返回格式，确保拿到视频链接
            play_url = data.get('data', {}).get('play') or data.get('url')
            if play_url and play_url.startswith('http'):
                return jsonify({
                    'code': 200,
                    'msg': '解析成功',
                    'data': {
                        'url': play_url
                    }
                })
            else:
                return jsonify({'code': -1, 'msg': '解析失败，未获取到无水印视频链接'})
        else:
            return jsonify({'code': -1, 'msg': f'解析接口请求失败，状态码：{parse_res.status_code}'})
    
    # 全局异常捕获（避免代码崩溃，返回友好提示）
    except Exception as e:
        return jsonify({'code': -1, 'msg': f'解析出错：{str(e)[:30]}'})
