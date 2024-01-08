from quart import Quart, request, jsonify, send_from_directory
import os

import base64
import urllib.parse
import hashlib
from html import escape, unescape
import uuid
import jwt
import colorsys
import datetime

app = Quart(__name__,static_folder='static')

@app.route('/uuid', methods=['GET'])
async def generate_uuid():
    return jsonify({"uuid": str(uuid.uuid4())})

@app.route('/base64', methods=['GET'])
async def process_base64():
    data = request.args.get('data')
    action = request.args.get('action', 'encode')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        if action == 'encode':
            result = base64.b64encode(data.encode()).decode()
        elif action == 'decode':
            result = base64.b64decode(data.encode()).decode()
        else:
            return jsonify({"error": "Invalid action. Use 'encode' or 'decode'"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/url', methods=['GET'])
async def process_url():
    data = request.args.get('data')
    action = request.args.get('action', 'encode')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        result = urllib.parse.quote(data) if action == 'encode' else urllib.parse.unquote(data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/md5', methods=['GET'])
async def process_md5():
    data = request.args.get('data')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        result = hashlib.md5(data.encode()).hexdigest()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sha256', methods=['GET'])
async def process_sha256():
    data = request.args.get('data')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        result = hashlib.sha256(data.encode()).hexdigest()
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/html', methods=['GET'])
async def process_html():
    data = request.args.get('data')
    action = request.args.get('action', 'encode')

    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        result = escape(data) if action == 'encode' else unescape(data)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/color-conversion', methods=['GET'])
async def color_conversion():
    color = request.args.get('color')
    format_to = request.args.get('format')

    if not color or not format_to:
        return jsonify({"error": "Missing color or format parameter"}), 400

    try:
        if format_to == 'rgb':
            # Assuming color is in hex format
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            return jsonify({"rgb": f"rgb({r}, {g}, {b})"})
        elif format_to == 'hex':
            # Assuming color is in rgb format
            rgb_values = color.replace('rgb', '').replace('(', '').replace(')', '').split(',')
            hex_color = f"#{int(rgb_values[0]):02x}{int(rgb_values[1]):02x}{int(rgb_values[2]):02x}"
            return jsonify({"hex": hex_color})
        else:
            return jsonify({"error": "Invalid format parameter"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/timestamp-conversion', methods=['GET'])
async def timestamp_conversion():
    timestamp = request.args.get('timestamp')
    format_str = request.args.get('format')

    if not timestamp or not format_str:
        return jsonify({"error": "Missing timestamp or format parameter"}), 400

    try:
        datetime_obj = datetime.datetime.fromtimestamp(int(timestamp))
        formatted_time = datetime_obj.strftime(format_str)
        return jsonify({"formatted_time": formatted_time})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/jwt-generate', methods=['POST'])
async def jwt_generate():
    payload = await request.get_json()
    jwt_secret = request.args.get('JWT_SECRET')

    if not payload:
        return jsonify({"error": "No payload provided"}), 400
    if not jwt_secret:
        return jsonify({"error": "No JWT_SECRET provided"}), 400

    try:
        token = jwt.encode(payload, jwt_secret, algorithm="HS256")
        return jsonify({"token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/jwt-verify', methods=['POST'])
async def jwt_verify():
    data = await request.get_json()
    token = data.get('token')
    jwt_secret = request.args.get('JWT_SECRET')

    if not token:
        return jsonify({"error": "No token provided"}), 400
    if not jwt_secret:
        return jsonify({"error": "No JWT_SECRET provided"}), 400

    try:
        decoded = jwt.decode(token, jwt_secret, algorithms=["HS256"])
        return jsonify({"decoded": decoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/legal', methods=['GET'])
async def legal():
    try:
        return await send_from_directory('./', 'legal.txt')
    except FileNotFoundError:
        return jsonify({"error": "Legal file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
