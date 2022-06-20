from Search_Youtube_Caption.pipeline.Steps.download_captions import DownloadCaptions
from Search_Youtube_Caption.pipeline.Steps.step import StepException
from Search_Youtube_Caption.pipeline.Steps.video_list import GetVideoList
from Search_Youtube_Caption.pipeline.Steps.read_caption import ReadCaption
from Search_Youtube_Caption.pipeline.pipeline import Pipeline
from Search_Youtube_Caption.utils import Utils
from Search_Youtube_Caption.pipeline.Steps.preflight import Preflight
from Search_Youtube_Caption.pipeline.Steps.postflight import Postflight

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


# TODO: get all video list from youtube api
# TODO: download video subtitles
# TODO: download youtube video
# TODO: edit video

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        Postflight(),
             ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()



