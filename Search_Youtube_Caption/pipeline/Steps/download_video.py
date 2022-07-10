import logging
import os, time
from threading import Thread

from pytube import YouTube

from .step import Step
from Search_Youtube_Caption.setting import VIDEO_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('Logger')
        start = time.time()
        threads = []
        for i in range(4):
            logger.info('registering process %d' % i)
            threads.append(Thread(target=self.download_yt, args=(data[i::4], inputs, utils)))
            # Second Method to work it the muti-threading
            # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            #     executor.submit(self.download_yt, yt, inputs, utils)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        logger.warning('took' +  str(end - start) + 'seconds')

        return data

    def download_yt(self, data, inputs, utils):
        logger = logging.getLogger('Logger')
        yt_set = set([found.yt for found in data])
        logger.info('videos to download' +  str(len(yt_set)))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                logger.info(f'found existing video file for {url}, skipping')
                continue
            else:
                logger.info('Downloading: ' + url)
                YouTube(url).streams.filter(res=inputs["resolution"]).first().download(output_path=VIDEO_DIR, filename=yt.id + '.mp4')
