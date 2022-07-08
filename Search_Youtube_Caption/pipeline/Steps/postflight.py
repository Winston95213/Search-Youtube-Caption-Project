import os

from Search_Youtube_Caption.pipeline.Steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        if inputs['clean_up']:
            os.remove("Search_Youtube_Caption/downloads/video")
            os.remove("Search_Youtube_Caption/downloads/captions")

            if not utils.video_file_exists():
                print("The video file clean up succeed")
            if not utils.caption_file_exists():
                print("The caption file clean up succeed")

        print('in Postflight')