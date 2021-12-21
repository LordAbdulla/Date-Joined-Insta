import requests, secrets
from user_agent import generate_user_agent
rs = requests.session()
print(''' 
                                           
    ____              ______            __    
   / __ \___ _      _/_  __/___  ____  / /____
  / / / / _ \ | /| / // / / __ \/ __ \/ / ___/
 / /_/ /  __/ |/ |/ // / / /_/ / /_/ / (__  ) 
/_____/\___/|__/|__//_/  \____/\____/_/____/  
                                              
            Tele : @DewTools | @LordAbdulla 
            ''')
dewx = input(' Enter The UserName : ')
head = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'cookie': f'csrftoken={secrets.token_hex(8)*2}; sessionid={secrets.token_hex(8)*2};',
    'user-agent': generate_user_agent(),
    }
info_user = f'https://www.instagram.com/{dewx}/?__a=1'
req = rs.get(info_user,headers=head).json()
dady= str(req['logging_page_id']).split('_')[1]

lord = f'https://o7aa.pythonanywhere.com/?id={dady}'

dadyx = rs.get(lord)
dewtools = dadyx.json()
datee = dewtools['data']
print(f' [+] The Date That {dewx} Joined Insta Is {datee}')


#Telegram : @DewTools
#Inst : @hr8k
#Github : github.com/LordAbdulla
