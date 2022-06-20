import os

from Search_Youtube_Caption.setting import CAPTION_DIR, VIDEO_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTION_DIR, self.id + '.txt')

    def get_video_filepath(self):
        return os.path.join(VIDEO_DIR, self.id + '.mp4')

    def __str__(self):
        return '<YT(' + self.id + ')>'

    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filePath=' + str(self.caption_filepath),
            'video_filePath=' + str(self.video_filepath)
        ])
        return '<Found(' + content + ')>'
