import logging
from datetime import datetime
import os,sys

log_dir="logs"
log_file_name=f"log_{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"
log_file_path=os.path.join(log_dir,log_file_name)

os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(level=logging.INFO,filename=log_file_path,
                    format="[%(asctime)s-%(name)s] : %(levelname)s %(message)s")