import os, time

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        existing_caption_counter = 0
        for url in data:
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                existing_caption_counter += 1
                print(f'found {existing_caption_counter} existing caption file')
                continue
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_covert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print("KeyError when download caption for", url)

            text_file = open(utils.get_video_id_from_url(url), 'w', encoding='utf-8')
            text_file.write(en_caption_covert_to_srt)
            text_file.close()
