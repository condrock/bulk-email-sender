==============================================================

# bulk-email-sender

This is a Python code that uses the smtplib and ssl libraries to send email through an SMTP (Simple Mail Transfer Protocol) server.

There are a number of variables that are initialized at the beginning of the code. 'to_addrs' is a list of destination email addresses that will receive emails. 'msg' is a MIMEMultipart object that is part of the email library. 'isi_email' is a string that contains the contents of the message from the email to be sent.

After that, a MIMEText object is created with email_content as its content, then it is attached to 'msg'. Then, the SMTP server is initiated using the ssl context that was created. Login to the server using the username and password stored in the 'config' file, then send an email using the sendmail() function with the variables 'from_addr', 'to_addrs' and 'msg.as_string()' as parameters. After that, the server is closed using the quit() function.

Finally, the message "Congratulations Your Email Sent Successfully" will be printed to the screen after the email sending process is complete.

==============================================================

# pengirim email massal

Ini adalah sebuah kode Python yang menggunakan library smtplib dan ssl untuk mengirim email melalui server SMTP (Simple Mail Transfer Protocol).

Terdapat sejumlah variabel yang diinisialisasi di awal kode. 'to_addrs' adalah list dari alamat email tujuan yang akan menerima email. 'msg' adalah sebuah objek MIMEMultipart yang merupakan bagian dari library email. 'isi_email' adalah string yang mengandung isi pesan dari email yang akan dikirim.

Setelah itu, sebuah objek MIMEText dibuat dengan isi_email sebagai isinya, lalu diattach ke 'msg'. Kemudian, server SMTP diinitiate dengan menggunakan context ssl yang telah dibuat. Login ke server dengan menggunakan username dan password yang tersimpan di dalam file 'config', lalu kirim email dengan menggunakan fungsi sendmail() dengan variabel 'from_addr', 'to_addrs', dan 'msg.as_string()' sebagai parameter. Setelah itu, server tersebut di-close dengan menggunakan fungsi quit().

Terakhir, pesan "Selamat Email Anda Berhasil Terkirim" akan dicetak ke layar setelah proses pengiriman email selesai.

==============================================================
