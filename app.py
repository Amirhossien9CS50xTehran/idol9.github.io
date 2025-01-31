from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    user_email = request.form['email']  # ایمیل فرستنده رو می‌گیریم
    message = request.form['message']  # پیامی که کاربر نوشته رو می‌گیریم
    
    # اطلاعات ایمیل خودت
    sender_email = 'your-email@example.com'
    sender_password = 'your-email-password'
    
    # تنظیمات ارسال ایمیل
    receiver_email = 'your-email@example.com'  # ایمیل خودت رو قرار می‌دی که دریافت‌کننده باشی
    
    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['To'] = receiver_email
    msg['Subject'] = 'New message from contact form'
    
    # پیام ایمیل رو تنظیم می‌کنیم
    body = f"Message from: {user_email}\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))
    
    # ارسال ایمیل
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # تنظیم برای Gmail
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        return 'Email sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
