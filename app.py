from Text_To_Speech_SRC.exception import TextSpeechException
import os,sys

try:
    print(1/0)
except Exception as e:
    print(TextSpeechException(e,sys))
    raise TextSpeechException(e,sys)
    