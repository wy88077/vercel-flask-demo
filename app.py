from flask import Flask, request, jsonify, render_template

# 导入全部平台
from api.wyy import parse_wyy
from api.douyin import parse_douyin
from api.kuaishou import parse_kuaishou
from api.xiaohongshu import parse_xiaohongshu
from api.weibo import parse_weibo

app = Flask(__name__)

# 主页前端
@app.route('/')
def index():
    return render_template('index.html')

# 网易云
@app.route('/api/wyy', methods=['GET'])
def wyy_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入网易云链接"}), 400
    try:
        res = parse_wyy(url)
        return jsonify({"code": 0, "data": res})
    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 500

# 抖音
@app.route('/api/douyin', methods=['GET'])
def douyin_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入抖音链接"}), 400
    try:
        res = parse_douyin(url)
        return jsonify({"code": 0, "data": res})
    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 500

# 快手
@app.route('/api/kuaishou', methods=['GET'])
def kuaishou_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入快手链接"}), 400
    try:
        res = parse_kuaishou(url)
        return jsonify({"code": 0, "data": res})
    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 500

# 小红书
@app.route('/api/xhs', methods=['GET'])
def xhs_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入小红书链接"}), 400
    try:
        res = parse_xiaohongshu(url)
        return jsonify({"code": 0, "data": res})
    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 500

# 微博
@app.route('/api/weibo', methods=['GET'])
def weibo_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"code": -1, "msg": "请传入微博链接"}), 400
    try:
        res = parse_weibo(url)
        return jsonify({"code": 0, "data": res})
    except Exception as e:
        return jsonify({"code": -1, "msg": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
