import boto3
import botocore
import pdfkit
from pathlib import Path
import os
import json
from flask import Flask
from flask_mail import Mail, Message

BASE_DIR = Path(__file__).resolve().parent

BASE_DIR_STORAGE = Path(__file__).resolve().parent

email_config_file = open(str(Path.joinpath(BASE_DIR, "credentials/email_config.json")))
email_config_file_json = json.load(email_config_file)

LOGO_URL = str(email_config_file_json["LOGO_URL"])
EMAIL = str(email_config_file_json["EMAIL_HOST_USER"])
PASSWORD = str(email_config_file_json["EMAIL_HOST_PASSWORD"])
EMAIL_NAME = str(email_config_file_json["EMAIL_NAME"])

FACEBOOK = str(email_config_file_json["FACEBOOK"])
TWITTER = str(email_config_file_json["TWITTER"])
INSTAGRAM = str(email_config_file_json["INSTAGRAM"])
BUCKET_FOLDER_NAME = str(email_config_file_json["BUCKET_FOLDER_NAME"])

credentials_conf_file = open(str(Path.joinpath(BASE_DIR, "credentials/aws_credentials.json")))
credentials_conf_json_file = json.load(credentials_conf_file)

AWS_ACCESS_KEY_ID = str(credentials_conf_json_file["aws_access_key_id"])
AWS_SECRET_ACCESS_KEY = str(credentials_conf_json_file["aws_secret_access_key"])

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

mail = Mail(app)

GSTIN = "07AAGFF2194N1Z1"
emailID = "sameeer.deshmukh@gmail.com"
custName = "Sameer Deshmukh"
custAddress = "Joshiwadi, Gopalnagar, Nagpur - 440022"
techName = "Nikhil Perkar"
invID = "INV000001"
orderDate = "23-Oct-2023"
orderId = "NGPEL000001"
total = 240
invoiceAmount = 259.61
numToWordsStr = "Two Hundred Fifty Nine Rupees"
CGST = 10.96
SGST = 10.96
subservices = ['subservices']
quantity = [1]
rate = [240]
amount = [240]
billamt = 100
discountAvailable = False
discStr = "You have been given a discount"
discountAmount = 50
hsn = "9618"
currentDate = "23-Oct-2023"
receiver_email = "sameeer.deshmukh@gmail.com"
trade = "Electrician"
GST = 5

# BUCKET_NAME = 'azulmanuserdata'
# KEY = BUCKET_FOLDER_NAME+'transactionimages/'+orderId+'/'
# mail_subject = 'AZULMAN Invoice'    
# s3 = boto3.client('s3', aws_access_key_id=str(credentials_conf_json_file["aws_access_key_id"]) , aws_secret_access_key=str(credentials_conf_json_file["aws_secret_access_key"]))

htmlstring = """
<html xmlns='http://www.w3.org/1999/xhtml'>
    <head>
        <meta charset='utf-8'>
            <title>Invoice Table</title>
        </head>
        <style>span:before{content:' '; display:inline-block; width:50px;}#itemTable{border-collapse: collapse; font-size: 12px; border: 1px solid black;}#itemTable th{border: 1px solid black; padding: 4px; text-align: center;}#itemTable td{border-right: 1px solid black; padding: 4px; text-align: center;}#totalTable{margin-left: auto; line-height: 1.5em; padding: 10px; padding-right: 28px; border: none; font-size: 12px;}#totalTable td{border: none;}</style>
        <body itemscope itemtype='http://schema.org/EmailMessage' style='position:relative; width: 600px;  height: fit-content; border: 2px solid black; font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif; -webkit-font-smoothing: antialiased;-webkit-text-size-adjust: none;'>
        <div style='width: 100%; border-bottom: 1px solid black; margin: 0 auto; text-align: center;'>
            <img src="""+LOGO_URL+""" alt='azulman_logo' width='100px' height='100px' style='display: inline-block; text-align: center; vertical-align: bottom; margin: 10px auto;'>
                <!-- <span></span> -->
            </div>
            <div id='custDetails' style='padding-left: 16px; padding-right: 16px;'>
                <h3 style='text-align: center; line-height: 0em;'>TAX INVOICE</h3>
                <div style='width: 245px; margin-left: 0; display: inline-block; line-height: 1.2em; font-size: 12px; vertical-align: top;'>
                    <p style='line-height: 0.6em;'>"""+custName+"""</p>
                    <p>"""+custAddress+"""</p>
                    <br>
                    <p style='line-height: 0.6em;>Trade: """+trade+"""</p>
                    <p style='line-height: 0.6em;>Technician: """+techName+"""</p>
                    </div>
                    <div style='width: 200px; margin-right: 0; margin-left: 100px; display: inline-block;line-height: 0.6em; font-size: 12px; vertical-align: top;'>
                    <p>Invoice No: """+invID+"""</p>
                    <p>Date: """+currentDate+"""</p>
                    <br>
                    <p>Order Date: """+orderDate+"""</p>
                    </div>
                    </div>
                    <table id='itemTable' style='width: 100%;'>
                        <tr>
                            <th style='border-left: none;'>Sr.</th>
                            <th>Description</th>
                            <th>HSN</th>
                            <th>Qty</th>
                            <th>Rate</th>
                            <th style='border-right: none;'>Amount</th>
                        </tr>"""
index = 0
for itemS,itemQ,itemR,itemA,itemH in zip(subservices,quantity,rate,amount,hsn):
    index +=1
    htmlstring = htmlstring + """<tr>
        <td style='border-left: none;'>
        """+str(index)+"""
        </td>
        <td style='text-align: left; margin-left: 16px; max-width: 180px;'>	
        """+itemS+"""
        </td>
        <td>
        """+itemH+"""
        </td>
        <td>
        """+str(itemQ)+"""
        </td>
        <td>
        """+str(itemR)+"""
        </td>
        <td style='border-right: none;'>
                """+"{:.2f}".format(itemA)+"""
        </td>
        </tr>"""
    """</table>"""
if discountAvailable:
    htmlstring = htmlstring + """<table id='totalTable'>
            <tr>
                <td style='text-align: left;'>Total</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(total)+"""
                </td>
            </tr>
            <tr>
                <td style='text-align: left;'>"""+discStr+"""</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(discountAmount)+"""
                </td>
            </tr>
            <tr>
                <td style='text-align: left;'>SGST ("""+"{:.2f}".format(GST/2)+"""%)</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(SGST)+"""
                </td>
            </tr>
            <tr>
                <td style='text-align: left;'>CGST ("""+"{:.2f}".format(GST/2)+"""%)</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(CGST)+"""
                </td>
            </tr>
            <tr>
                <td style='text-align: left;'>Parts Bill</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(billamt)+"""
                </td>
            </tr>
            <tr style='font-weight: bold;'>
                <td style='text-align: left;'>Invoice Amount</td>
                <td style='text-align: right;'>
                    """+"{:.2f}".format(invoiceAmount)+"""
                </td>
            </tr>
            <tr>
                <td style='text-align: left;'>
                    """+numToWordsStr+""" only
                </td>
                <td>
                </td>
            </tr>
        </table>"""
else:
    htmlstring = htmlstring + """<table id='totalTable'>
            <tr>
                <td style='text-align: left;'>Total</td>
                <td style='text-align: right;'>"""+"{:.2f}".format(total)+"""</td>
            </tr>
            <tr>
                <td style='text-align: left;'>SGST ("""+"{:.2f}".format(GST/2)+"""%)</td>
                <td style='text-align: right;'>"""+"{:.2f}".format(SGST)+"""</td>
            </tr>
            <tr>
                <td style='text-align: left;'>CGST ("""+"{:.2f}".format(GST/2)+"""%)</td>
                <td style='text-align: right;'>"""+"{:.2f}".format(CGST)+"""</td>
            </tr>
            <tr>
            <td style='text-align: left;'>Parts Bill</td>
            <td style='text-align: right;'>
                """+"{:.2f}".format(billamt)+"""
            </td>
            </tr>
            <tr style='font-weight: bold;'>
                <td style='text-align: left;'>Invoice Amount</td>
                <td style='text-align: right;'>"""+"{:.2f}".format(invoiceAmount)+"""</td>
            </tr>
            <tr>
                <td style='text-align: left;'>
                """+numToWordsStr+""" only</td>
                <td></td>
            </tr>
        </table>"""
htmlstring = htmlstring + """<div style='position:absolute; width: 100%; font-size: 12px; border-top: 1px solid black; height: 40px; bottom: 90px;'>
                        <div style='padding-left: 16px; float:left; margin-top: 12px;'>Subject to Nagpur Jurisdiction</div>
                        <div style='padding-right: 16px; float: right; margin-top: 12px;'>
                            <b>For SBE Technologies India Pvt. Ltd.</b>
                        </div>
                    <div style='display: inline-block; text-align: center; line-height: 0.3em; width: 100%; border-top: 1px solid black; margin: 10px auto;'>
                    <h2 style='line-height: 0.5em;'>SBE Technologies India Pvt. Ltd.</h2>
                    <p style='font-size: 12px; letter-spacing: 0.6px;'>D-104, Himalaya Valley, Hindustan Colony,</p>
                    <p style='font-size: 12px; letter-spacing: 0.6px;'>Amravati Road, Nagpur - 440033, Maharashtra (27)</p>
                    <p style='font-size: 12px; letter-spacing: 0.6px;'>GSTIN:
                        """+GSTIN+"""</p>
                </div>
                </div>
            </body>
        </html>
"""



options = {
    'page-size': 'A5',
    'margin-top': '0.50in',
    'margin-right': '0.50in',
    'margin-bottom': '0.50in',
    'margin-left': '0.50in',
    'encoding': "UTF-8",
}

# session = boto3.Session(
# 	aws_access_key_id=AWS_ACCESS_KEY_ID,
# 	aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
# )
# s3 = session.resource('s3')
# file = []

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
pdfkit.from_string(htmlstring,str(Path.joinpath(BASE_DIR_STORAGE, "invoice.pdf")), configuration=config, options=options)




# s3.meta.client.upload_file(Filename=str(Path.joinpath(BASE_DIR_STORAGE, "invoice.pdf")), Bucket=BUCKET_NAME, Key=KEY+'invoice.pdf')

# try:
# 	bucket = s3.Bucket(BUCKET_NAME)
# 	for obj in bucket.objects.filter(Prefix = KEY):
# 		key = obj.key
# 		if len(BUCKET_FOLDER_NAME) == 0:
# 			x = key.split('/',2)[2]
# 		else:
# 			x = key.split('/',3)[3]
# 		file.append(x)
# 		bucket.download_file(obj.key,str(Path.joinpath(BASE_DIR_STORAGE, x)))
# 	msg = Message(mail_subject, sender = (EMAIL_NAME,EMAIL), recipients = [receiver_email])
# 	msg.html ="""
#         <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
#            <head>
#               <meta charset="utf-8">
#               <meta name="viewport" content="width=device-width">
#               <meta http-equiv="X-UA-Compatible" content="IE=edge">
#               <meta name="x-apple-disable-message-reformatting">
#               <title></title>
#            </head>
#            <style>html, body{width: 100%; padding: 16px; height: fit-content; box-sizing: border-box; font-size: 14px;}img{margin: 0; display: block;}.msg-div{line-height: 0.5em;}.passAssistance{float: right; margin-top: 80px; font-weight: bolder;}</style>
#            <body style=" font-family: Arial, Helvetica, sans-serif; padding: 16px; width: 100%;padding: 16px; height: fit-content; box-sizing: border-box; margin-top:16px; margin-bottom: 16px; background-color: white;margin: 0 auto; max-width: 600px;"> <div style="width: inherit; padding-bottom: 10px; border-bottom: 1px solid #bfbfbf;"> 
#            <img src="""+LOGO_URL+""" alt="azulman_logo" width="100px" height="100px" style="display: inline-block;">
#            <div style="float: right; margin-top: 86px;">Date: """+currentDate+"""</div></div><br>
#            <p style="font-size: large; font-weight: bold;">Hi """+ custName +""", Thank you for ordering on AZULMAN!</p>
#            <p style="line-height: 1.5em;">Payment received for the Order ID: """+ orderId +"""</p><br>
#            <hr>
#            <p style="text-align:center">
#            <a href="""+FACEBOOK+""" style="padding: 5px 10px;text-decoration:none" rel="noreferrer" target="_blank"><img alt="Facebook" src="https://azulmanimages.s3.ap-south-1.amazonaws.com/facebook.png" title="Facebook" width="25" border="0" style="border:0;height:auto;outline:none;text-decoration:none"> </a>
#            <a href="""+TWITTER+""" style="padding: 5px 10px;text-decoration:none" rel="noreferrer" target="_blank"><img alt="Twitter" src="https://azulmanimages.s3.ap-south-1.amazonaws.com/twitter.png" title="Twitter" width="25" border="0" style="border:0;height:auto;outline:none;text-decoration:none"></a>
#            <a href="""+INSTAGRAM+""" style="padding: 5px 10px;text-decoration:none" rel="noreferrer" target="_blank"><img alt="Instagram" src="https://azulmanimages.s3.ap-south-1.amazonaws.com/instagram.png" title="Instagram" width="25" border="0" style="border:0;height:auto;outline:none;text-decoration:none"></a>
#            </p>
#            <p style="text-align:center; line-height: 1.5em;"> Need Help? You may <a href="mailto:"""+EMAIL+"""" style="cursor: pointer; color: #007bff; text-decoration: none;" onmouseover='this.style.textDecoration="none";this.style.color="#3e4095"' onmouseout='this.style.textDecoration="none";this.style.color="#007bff"' rel="noreferrer" target="_blank">email us</a> or visit us <a href="https://www.azulman.com" style="cursor: pointer; color: #007bff; text-decoration: none;" onmouseover='this.style.textDecoration="none";this.style.color="#3e4095"' onmouseout='this.style.textDecoration="none";this.style.color="#007bff"' rel="noreferrer" target="_blank">here</a> </p>
#            </div></body>
#         </html>
#     """
# 	# msg.body = "Payment received. Thank you for using AZULMAN!"
# 	for filename in file:
# 		if filename == 'invoice.pdf':
# 			docc_type = "application/pdf"
# 		else:
# 			docc_type = "image/jpg"
# 		with app.open_resource(filename) as fp:
# 			msg.attach(filename,docc_type,fp.read())
# 	mail.send(msg)
# 	for filename in file:
# 		os.remove(str(Path.joinpath(BASE_DIR_STORAGE, filename)))
# except botocore.exceptions.ClientError as e:
# 	if e.response['Error']['Code'] == "404":
# 		print("The object does not exist.")
# return "Uploaded!"



