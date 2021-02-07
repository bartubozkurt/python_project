import smtplib
sender_mail  = input("Enter your gmail: ")
recievers_mail = input("Enter receivers gmail: ")

message = """ 
From: From Person %s
To: To Person  %s
Subject: Sending SMTP  email
this is  a test e-mail message.
"""%(sender_mail,recievers_mail)
try:
    password = input('Enter the password: ');
    smtpObj =  smtplib.SMTP('gmail.com',587)
    smtpobj.login(sender_mail,password)
    smtpObj.sendmail(sender_mail,recievers_mail,message)
    print("Succesfully sent mail")
except:
    print("Error: unable to send mail")