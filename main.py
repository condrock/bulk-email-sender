import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import username_email, pass_email

# alamat email tujuan
to_addrs = [
    'target1@gmail.com',
    'target2@gmail.com',
    'target3@gmail.com',
    'target4@gmail.com',
    'target5@gmail.com',
]

# subject dan nama pengirim
msg = MIMEMultipart("alternative")
msg['Subject'] = 'Your Subject'
msg['From'] = 'Your Name'
msg['To'] = ', '.join(to_addrs)

# isi email
isi_email = "Bagian ini adalah isi dari pesan email yang akan Anda kirim."

# tambahkan isi email sebagai teks
pesan = MIMEText(isi_email)
msg.attach(pesan)

# kirim email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username_email, pass_email)
    server.sendmail(from_addr=username_email,
                    to_addrs=to_addrs,
                    msg=msg.as_string())
    server.quit()

    print("Selamat Email Anda Berhasil Terkirim")