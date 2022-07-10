import os, time, logging
from threading import Thread

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('Logger')
        threads = []
        start = time.time()

        for yt in data:
            logger.info('downloading caption for' + yt.id)
            if utils.caption_file_exists(yt):
                logger.info('found existing caption file')
                continue
            logger.info(f"registering threads for downloading caption...")
            threads.append(Thread(target=self.get_caption, args=(yt,)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        end = time.time()
        logger.info('took' +  str(end - start) + 'seconds')

        return data

    def get_caption(self, yt):
        logger = logging.getLogger('Logger')
        try:
            logger.info('Downloading caption for' + yt.id)
            source = YouTube(yt.url)
            en_caption = source.captions['a.en']

            with open(yt.caption_filepath, 'w', encoding='utf-8') as f:
                f.write(en_caption.generate_srt_captions())

        except (KeyError, AttributeError):
            logger.debug('Error when downloading caption for: ' + yt.url)



