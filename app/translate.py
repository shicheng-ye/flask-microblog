import json
import requests
from flask import current_app
from flask_babel import _
from hashlib import md5
import random


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def get_language_code(lang):
    # Barber to Baidu
    language_codes = {  'es': 'spa',
                        'en': 'en',
                        'zh': 'zh',
                        'zh_Hans_CN': 'zh'
                    }
    return language_codes[lang]


def translate(query, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
        not current_app.config['MS_TRANSLATOR_KEY'] or \
        'MS_TRANSLATOR_ID' not in current_app.config or \
        not current_app.config['MS_TRANSLATOR_ID']        :
        return _('Error: the translation service is not configured.')
    source_language = get_language_code(source_language)
    dest_language = get_language_code(dest_language)
    salt = random.randint(32768, 65536)
    sign = make_md5(current_app.config['MS_TRANSLATOR_ID'] + query 
                    + str(salt) + current_app.config['MS_TRANSLATOR_KEY'])
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': current_app.config['MS_TRANSLATOR_ID'], 'q': query, 'from': source_language, 
                'to': dest_language, 'salt': salt, 'sign': sign}
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    if 'error_code' in result:
        return _('Error {}: the translation service failed.'.format(result['error_code'])) 
    # return the first paragraph
    return result['trans_result'][0]['dst']