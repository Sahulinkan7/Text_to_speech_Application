from dataclasses import dataclass
from Text_To_Speech_SRC.constants import APPLICATION_NAME,ARTIFACT_DIR,AUDIO_DIR,TEXT_DIR
import os,sys

CURRENT_DIR = os.getcwd()


@dataclass
class TTSApplicationConfig:
    application_name : str = APPLICATION_NAME
    artifact_dir : str = os.path.join(CURRENT_DIR,application_name,ARTIFACT_DIR)
    audio_dir : str = os.path.join(artifact_dir,AUDIO_DIR)
    text_dir : str = os.path.join(artifact_dir,TEXT_DIR)