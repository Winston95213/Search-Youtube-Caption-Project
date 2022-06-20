from pytube import YouTube

from .step import Step
from Search_Youtube_Caption.setting import VIDEO_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('video to download= ', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f"found existing video file for {url} -> skipping")
                continue

            print('downloading ', url)
            YouTube(url).streams.filter(res="360p").first().download(output_path=VIDEO_DIR, filename=yt.id + '.mp4')

        return data
