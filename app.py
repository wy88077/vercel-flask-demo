from flask import Flask, request, jsonify
import traceback

# 导入各平台解析模块
from api.wyy import parse_wyy
from api.douyin import parse_douyin
from api.kuaishou import parse_kuaishou
from api.xiaohongshu import parse_xiaohongshu
from api.weibo import parse_weibo

app = Flask(__name__)

# 根路由（测试用）
@app.route('/')
def index():
    return """
    ✅ 去水印服务部署成功！<br>
    接口使用示例：<br>
    抖音：/api/douyin?url=抖音链接<br>
    快手：/api/kuaishou?url=快手链接<br>
    小红书：/api/xhs?url=小红书链接<br>
    微博：/api/weibo?url=微博链接<br>
    网易云：/api/wyy?url=网易云链接
    """

# 网易云解析接口
@app.route('/api/wyy', methods=['GET'])
def wyy_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入网易云链接"}), 400
    try:
        result = parse_wyy(url)
        return jsonify({"code": 0, "data": result})
    except Exception as e:
        return jsonify({"code": -1, "msg": f"解析失败：{str(e)}"}), 500

# 抖音解析接口
@app.route('/api/douyin', methods=['GET'])
def douyin_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入抖音链接"}), 400
    try:
        result = parse_douyin(url)
        return jsonify({"code": 0, "data": result})
    except Exception as e:
        return jsonify({"code": -1, "msg": f"解析失败：{str(e)}"}), 500

# 快手解析接口
@app.route('/api/kuaishou', methods=['GET'])
def kuaishou_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入快手链接"}), 400
    try:
        result = parse_kuaishou(url)
        return jsonify({"code": 0, "data": result})
    except Exception as e:
        return jsonify({"code": -1, "msg": f"解析失败：{str(e)}"}), 500

# 小红书解析接口
@app.route('/api/xhs', methods=['GET'])
def xhs_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入小红书链接"}), 400
    try:
        result = parse_xiaohongshu(url)
        return jsonify({"code": 0, "data": result})
    except Exception as e:
        return jsonify({"code": -1, "msg": f"解析失败：{str(e)}"}), 500

# 微博解析接口
@app.route('/api/weibo', methods=['GET'])
def weibo_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入微博链接"}), 400
    try:
        result = parse_weibo(url)
        return jsonify({"code": 0, "data": result})
    except Exception as e:
        return jsonify({"code": -1, "msg": f"解析失败：{str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
