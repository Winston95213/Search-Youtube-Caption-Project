import os, logging

from Search_Youtube_Caption.pipeline.Steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('Logger')
        if inputs['clean_up']:
            os.remove("Search_Youtube_Caption/downloads/video")
            os.remove("Search_Youtube_Caption/downloads/captions")

            if not utils.video_file_exists():
                logger.warning("The video file clean up succeed")
            if not utils.caption_file_exists():
                logger.warning("The caption file clean up succeed")

        logger.info('in Postflight')