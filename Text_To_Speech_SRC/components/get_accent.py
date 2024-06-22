from Text_To_Speech_SRC.logger import logging
from Text_To_Speech_SRC.exception import TextSpeechException

import os,sys  


def get_accent_tld(user_input):
    try:
        accent_input={
            'Australian':'com.au',
            'South Africa':'co.za',
            'British':'co.uk',
            'Indian':'co.in',
            'Canadian':'ca',
            'Irish':'ie',
            'Spanish':'es'
        }
        
        tld=accent_input[user_input]
        return tld
    
    except Exception as e:
        raise TextSpeechException(e,sys)
    
    
def get_accent_list():
    try:
        accent = ['Australian','South Africa','British','Indian','Canadian','Irish','Spanish']
        return accent
    except Exception as e:
        raise TextSpeechException(e,sys)