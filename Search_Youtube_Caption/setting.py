import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_KEY2 = os.getenv('API_KEY2')
User_Agent = os.getenv('USER_AGENT')


DOWNLOAD_DIR = 'downloads'
VIDEO_DIR = os.path.join(DOWNLOAD_DIR, 'video')
CAPTION_DIR = os.path.join(DOWNLOAD_DIR, 'captions')
