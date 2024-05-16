from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mail-send', methods=['POST'])
def handle_post_request():
    # 요청의 JSON 본문에서 auth code와 emailAddress 추출
    data = request.get_json()
    auth_code = data.get('authCode')
    email_address = data.get('emailAddress')
    
    # 응답 데이터 생성
    response_data = {
        'authCode': auth_code,
        'emailAddress': email_address
    }
    
    # JSON 응답 반환
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)