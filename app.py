from flask import Flask, request, jsonify
from api.wyy import parse_wyy  # 只导入你需要的解析函数

app = Flask(__name__)

# 根路由（保留！）
@app.route('/')
def index():
    return "✅ 部署成功！"

# 网易云音乐解析接口
@app.route('/api/wyy', methods=['GET'])
def wyy_parse():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "请传入 url 参数"}), 400
    
    try:
        result = parse_wyy(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
