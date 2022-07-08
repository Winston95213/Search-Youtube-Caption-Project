import os

from Search_Youtube_Caption.setting import CAPTION_DIR, VIDEO_DIR, DOWNLOAD_DIR, OUTPUT_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEO_DIR, exist_ok=True)
        os.makedirs(CAPTION_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOAD_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def caption_file_exists(self, yt):
        file_path = yt.caption_filepath
        return os.path.exists(file_path) and os.path.getsize(file_path) > 0

    def video_file_exists(self, yt):
        file_path = yt.video_filepath
        return os.path.exists(str(file_path)) and os.path.getsize(file_path) > 0

    def get_output_filepath(self, channel_id, search_word):
        return os.path.join(OUTPUT_DIR, f"{channel_id}_{search_word}.mp4")

    def output_file_exist(self, id):
        file_path = os.path.join(OUTPUT_DIR, id+"mp.4")
        return os.path.exists(str(file_path)) and os.path.getsize(file_path) > 0
