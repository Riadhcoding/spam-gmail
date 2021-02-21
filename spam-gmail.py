import smtplib
i = "your email"
pw = "your password "
targat = ("SEND TO EMAIL : ")
msg = input ("MESSAGE: ")
number = int(input('ENTER NUMBERS MESSGES :'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(i,pw)
for i in range(number):
    server.sendmail(i,targat,msg)