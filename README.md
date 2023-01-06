==============================================================

# bulk-email-sender

This is a Python code that uses the smtplib and ssl libraries to send email through an SMTP (Simple Mail Transfer Protocol) server.

There are a number of variables that are initialized at the beginning of the code. 'to_addrs' is a list of destination email addresses that will receive emails. 'msg' is a MIMEMultipart object that is part of the email library. 'isi_email' is a string that contains the contents of the message from the email to be sent.

After that, a MIMEText object is created with email_content as its content, then it is attached to 'msg'. Then, the SMTP server is initiated using the ssl context that was created. Login to the server using the username and password stored in the 'config' file, then send an email using the sendmail() function with the variables 'from_addr', 'to_addrs' and 'msg.as_string()' as parameters. After that, the server is closed using the quit() function.

Finally, the message "Congratulations Your Email Sent Successfully" will be printed to the screen after the email sending process is complete.

Tips:

Use application passwords

Application passwords in Gmail are special passwords that can be used to access your Gmail account from third-party applications or services.

To use an application password on Gmail, you must first ensure that the application or service you are going to use has been authorized by Gmail to access your account. After that, you can follow these steps:

1. Open your Gmail account.
2. Click the gear icon at the top right of the screen, then select "Account Settings".
3. Select the "Security" tab.
4. Scroll down until you find the "Access Apps and Services" section.
5. Click the "Create Application Password" button.
6. You will be given a new application password that can be used to access your Gmail account from third-party applications or services.
7. Copy the application password that has been created, then paste it into the column provided in the application or service that you will use.
8. Done.

==============================================================

# pengirim email massal

Ini adalah sebuah kode Python yang menggunakan library smtplib dan ssl untuk mengirim email melalui server SMTP (Simple Mail Transfer Protocol).

Terdapat sejumlah variabel yang diinisialisasi di awal kode. 'to_addrs' adalah list dari alamat email tujuan yang akan menerima email. 'msg' adalah sebuah objek MIMEMultipart yang merupakan bagian dari library email. 'isi_email' adalah string yang mengandung isi pesan dari email yang akan dikirim.

Setelah itu, sebuah objek MIMEText dibuat dengan isi_email sebagai isinya, lalu diattach ke 'msg'. Kemudian, server SMTP diinitiate dengan menggunakan context ssl yang telah dibuat. Login ke server dengan menggunakan username dan password yang tersimpan di dalam file 'config', lalu kirim email dengan menggunakan fungsi sendmail() dengan variabel 'from_addr', 'to_addrs', dan 'msg.as_string()' sebagai parameter. Setelah itu, server tersebut di-close dengan menggunakan fungsi quit().

Terakhir, pesan "Selamat Email Anda Berhasil Terkirim" akan dicetak ke layar setelah proses pengiriman email selesai.

Tips:

Gunakan password aplikasi

Password aplikasi pada Gmail adalah password khusus yang dapat digunakan untuk mengakses akun Gmail Anda dari aplikasi atau layanan pihak ketiga. 

Untuk menggunakan password aplikasi pada Gmail, pertama-tama Anda harus memastikan bahwa aplikasi atau layanan yang akan Anda gunakan telah diizinkan oleh Gmail untuk mengakses akun Anda. Setelah itu, Anda dapat mengikuti langkah-langkah berikut:

1. Buka akun Gmail Anda.
2. Klik ikon roda gigi di bagian kanan atas layar, lalu pilih "Pengaturan Akun".
3. Pilih tab "Keamanan".
4. Scroll ke bawah hingga menemukan bagian "Akses Aplikasi dan Layanan".
5. Klik tombol "Buat Password Aplikasi".
6. Anda akan diberikan password aplikasi baru yang dapat digunakan untuk mengakses akun Gmail Anda dari aplikasi atau layanan pihak ketiga.
7. Salin password aplikasi yang telah dibuat, lalu paste-kan ke dalam kolom yang tersedia di aplikasi atau layanan yang akan Anda gunakan.
8. Selesai.

==============================================================
