import random
import requests

ua = random.choice(
    [ua for ua in requests.get('https://fake-useragent.herokuapp.com/browsers/0.1.11').json()['browsers']['chrome']])


# discord token change this
Authorization = 'token_here'

# text in your status [after time]
text_after_time = 'YOU NEED CHANGE "json_data" in main.py file (line 17) ' \
                  'CHANGE DATA AFTER "bio:"'

# dont change
headers = {
    'X-Debug-Options': 'bugReporterEnabled',
    'Authorization': Authorization,
    'User-Agent': ua,
    'X-Discord-Locale': 'ru',
    'Accept': '*/*',
}
