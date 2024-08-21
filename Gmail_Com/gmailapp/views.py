from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        sender_email = request.POST.get('sender-email')
        receiver_email = request.POST.get('receiver-email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'sender_email': sender_email,
            'receiver_email': receiver_email,
            'subject': subject,
            'message': message
        }
        message_content = '''
        New message: {}

        From: {} 
        '''.format(data['message'], data['sender_email'])
        
        send_mail(
            data['subject'],
            message_content,
            data['sender_email'],  # Sender's email
            [data['receiver_email']],  # Receiver's email
            fail_silently=False,
        )
        return HttpResponse("""
             <html>
            <head>
                <title>Email Sent</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        font-family: Arial, sans-serif;
                        background: linear-gradient(135deg, #df7d7d, #7aea92, #ff00ff,#cfe077);
                    }
                    h1 {
                        color: #333;
                        text-align: center;
                    }
                </style>
            </head>
            <body>
                <h1>Your email was sent successfully.</h1>
            </body>
            </html>
        """)
        
    
    return render(request, 'index.html')
