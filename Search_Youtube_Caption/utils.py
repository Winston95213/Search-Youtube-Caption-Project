import os

from Search_Youtube_Caption.setting import CAPTION_DIR, VIDEO_DIR, DOWNLOAD_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)

    def get_video_list_filepaths(self, channel_id):
        return os.path.join(DOWNLOAD_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_caption_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self, url):
        return os.path.join(CAPTION_DIR, self.get_video_id_from_url(url) + '.txt')

    def caption_file_exists(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
