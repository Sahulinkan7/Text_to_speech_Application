from Text_To_Speech_SRC.logger import logging
from Text_To_Speech_SRC.exception import TextSpeechException
import os,sys
from Text_To_Speech_SRC.entity.config_entity import TTSApplicationConfig
from Text_To_Speech_SRC.constants import TEXT_FILE_NAME
from gtts import gTTS
from Text_To_Speech_SRC.constants import CURRENT_TIME
import base64
from datetime import datetime

class TextToSpeechApplication:
    def __init__(self,app_config = TTSApplicationConfig()) -> None:
        try:
            self.app_config=app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir=app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            logging.error(f"{TextSpeechException(e,sys)}")
            raise TextSpeechException(e,sys)
        
    def get_text_to_speech(self,text,accent):
        try:
            current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            text_file_name = TEXT_FILE_NAME
            os.makedirs(self.text_dir,exist_ok=True)
            text_file_path = os.path.join(self.text_dir,text_file_name)
            with open(text_file_path,'a+') as file:
                file.write(f"\n{current_time}: {text}")
                
            # creating object for gtts
            
            tts=gTTS(text=text,lang='en',tld=accent)
            
            audio_file_name = f"converted_file_{current_time}.mp3"
            os.makedirs(self.audio_dir,exist_ok=True)
            audio_path = os.path.join(self.audio_dir,audio_file_name)
            
            tts.save(audio_path)
            
            with open(audio_path,'rb') as file:
                my_string = base64.b64encode(file.read())
            return my_string
        
        except Exception as e:
            logging.error(f"{TextSpeechException(e,sys)}")
            raise TextSpeechException(e,sys)
        
