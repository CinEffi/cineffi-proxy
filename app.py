from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

@app.route('/mail-send', methods=['POST'])
def handle_post_request():
    print("Request received from:", request.remote_addr)

    # 요청의 JSON 본문에서 auth code와 emailAddress 추출
    data = request.get_json()
    auth_code = data.get('authCode')
    email_address = data.get('emailAddress')
    
    # 응답 데이터 생성
    response_data = {
        'authCode': auth_code,
        'emailAddress': email_address
    }

    send_email(email_address, auth_code)
    
    # JSON 응답 반환
    return jsonify(response_data), 200

def send_email(recipient_email, auth_code):
    # SMTP 서버 설정
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'skwd1012@gmail.com' # 보내는 이메일 주소
    sender_password = 'tboxbeusjvbysajd' # 보내는 이메일의 비밀번호 또는 앱 비밀번호

    # 이메일 메시지 생성
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = '이메일 인증'

    # 이메일 본문 생성
    body = ""
    body += "<h3>요청하신 인증 번호입니다.</h3>"
    body += f"<h1>{auth_code}</h1>"
    body += "<h3>감사합니다.</h3>"

    # HTML 본문 첨부
    msg.attach(MIMEText(body, 'html'))

    try:
        # SMTP 서버에 연결 및 로그인
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # 이메일 전송
        server.send_message(msg)
        print('Email sent successfully')

        # SMTP 서버 연결 종료
        server.quit()

    except Exception as e:
        print(f'Failed to send email: {e}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)


