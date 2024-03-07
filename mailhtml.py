from smtplib import SMTP_SSL
from email.message import EmailMessage
import pandas as pd

sender='1694547.harshavardhan@gmail.com'
rec='memerversetv@gmail.com'
password="ulpx inhs fwkk scph" # This is not the gmail password turn on two step authentication down there you will find app passwords generate a app password with any random name you will get one password generated use that password here

df=pd.read_csv('./demo.csv')
for ind, row in df.iterrows():
    mail = EmailMessage()
    mail['Subject'] = 'ACM X GDSC'
    mail['From'] = sender
    mail['To'] = row['email']#add the column name in the excel which has the emails
    html = f"""
            <!DOCTYPE html>
        <html lang="en">
        
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Hello World Page</title>
        </head>
        
        <body>
            <img src='https://res.cloudinary.com/startup-grind/image/fetch/c_scale,w_2560/c_crop,h_650,w_2560,y_0.0_mul_h_sub_0.0_mul_650/c_crop,h_650,w_2560/c_fill,dpr_2.0,f_auto,g_center,q_auto:good/https://res.cloudinary.com/startup-grind/image/upload/c_fill%2Cdpr_2.0%2Cf_auto%2Cg_center%2Cq_auto:good/v1/gcs/platform-data-dsc/chapter_banners/GDSC%2520chapter%2520banner_Ljgs628.jpg' alt='GDSC logo'width="1080px"/>
            <h1>Hello {row['name']}!</h1>
            <p>This is a simple HTML page.</p>
        </body>
        
        </html>"""
    mail.add_alternative(html,subtype='html')
    with SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(mail)
        smtp.close()