import os

from pprint import pprint

from .step import Step
from Search_Youtube_Caption.setting import CAPTION_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTION_DIR):
            captions = {}
            with open(os.path.join(CAPTION_DIR, caption_file), 'r') as f:
                time_line = False
                caption = None
                time = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue

                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False

            data[caption_file] = captions

        pprint(data)
        return data
