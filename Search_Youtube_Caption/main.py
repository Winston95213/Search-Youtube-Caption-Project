from Search_Youtube_Caption.pipeline.Steps.step import StepException
from Search_Youtube_Caption.pipeline.Steps.video_list import GetVideoList
from Search_Youtube_Caption.pipeline.pipeline import Pipeline

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
        GetVideoList(),
             ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()



