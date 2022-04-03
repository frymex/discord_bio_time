from datetime import datetime
import family
import requests

global json_data

print(f"""Status: Successfully
User-agent: {family.ua}
Created by: t.me/cazqev""")

last = '2022-04-03 19:29:49'

while True:
    date, time = str(datetime.now().date()), str(datetime.now().time())[:5]
    if date + ' ' + time != last:
        last = date + ' ' + time
        json_data = {
            'bio': f'⌚ NOW: {last}\n'
                   f'💫 MY MAIL: t_frymex@protonmail.com',
        }
        response = requests.patch('https://discord.com/api/v9/users/@me', headers=family.headers,
                                  json=json_data)


