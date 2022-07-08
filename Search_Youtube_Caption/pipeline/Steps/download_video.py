import os, time
from threading import Thread

from pytube import YouTube

from .step import Step
from Search_Youtube_Caption.setting import VIDEO_DIR




class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        threads = []
        for i in range(4):
            print('registering process %d' % i)
            threads.append(Thread(target=self.download_yt, args=(data[i::4], inputs, utils)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

    def download_yt(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            else:
                print('Downloading: ', url)
                YouTube(url).streams.filter(res=inputs["resolution"]).first().download(output_path=VIDEO_DIR, filename=yt.id + '.mp4')
