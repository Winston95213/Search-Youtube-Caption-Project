import time, sys, getopt, logging
sys.path.append('../')   # For execute command line argument function

from Search_Youtube_Caption.pipeline.Steps.preflight import Preflight
from Search_Youtube_Caption.pipeline.Steps.video_list import GetVideoList
from Search_Youtube_Caption.pipeline.Steps.initialize_yt import InitialzeYT
from Search_Youtube_Caption.pipeline.Steps.download_captions import DownloadCaptions
from Search_Youtube_Caption.pipeline.Steps.read_caption import ReadCaption
from Search_Youtube_Caption.pipeline.Steps.search import Search
from Search_Youtube_Caption.pipeline.Steps.download_video import DownloadVideos
from Search_Youtube_Caption.pipeline.Steps.edit_video import EditVideo
from Search_Youtube_Caption.pipeline.Steps.postflight import Postflight
from Search_Youtube_Caption.pipeline.Steps.step import StepException
from Search_Youtube_Caption.pipeline.Steps.video_list import GetVideoList
from Search_Youtube_Caption.pipeline.pipeline import Pipeline
from Search_Youtube_Caption.utils import Utils


CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"

# TODO: get all video list from youtube api
# TODO: download video subtitles
# TODO: download youtube video
# TODO: edit video

def print_usage():
    print("python3 main.py OPTIONS")
    print("OPTIONS:")

    print("{:>6}{:<12}{}".format('-i', '--id', 'channel id of the youtube channel to download video and youtube'))
    print("{:>6}{:<12}{}".format('-s', '--search', 'Search the word in the video to combine the clips'))
    print("{:>6}{:<12}{}".format('-l', '--limit', 'The amount of video limitation to download'))
    print("{:>6}{:<12}{}".format('-c', '--clean', 'clean up the caption file and video file'))
    print("{:>6}{:<12}{}".format('-r', '--resolution', 'choose the resolution in of the video'))

def config_logger():
    logger = logging.getLogger('Logger')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

    file_handler = logging.FileHandler('Search_Youtube_Caption.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)





def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': "incredible",
        'limit': 20,
        'clean_up': False,
        'resolution': '360p',
    }

    short_opts = "c:s:l:i:r:h"
    long_opts = "help id= search= limit= clean= resolution=".split()


    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print('python main.py -c <channel id> -s <search_word> -l <limitation> -c <clean up>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--id"):
            inputs['channel_id'] = arg
        elif opt in ("-s", "--search"):
            inputs['search_word'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = arg
        elif opt in ("-c", "--clean"):
            inputs['clean_up'] = arg
        elif opt in ("-r", "--resolution"):
            res = ("144p", "240p", "360p", "480p", "720p", "1080p")
            if arg not in res:
                print("ArgumentError > please check your resolution argument and make sure choose a format in ", res)
                sys.exit(2)
            else:
                inputs['resolution'] = arg

    config_logger()
    utils = Utils()
    if utils.output_file_exist(inputs['channel_id']):
        ans = input('Clips video for this search term of this channel already existed.\
                        \nStill want to proceed?(Y/N)-->')
        if ans == 'y' or ans == 'Y':
            process_request(inputs, utils)
        else:
            print('Exiting program..')
            return
    else:
        process_request(inputs, utils)

def process_request(user_input, utili_object):
    steps = [
        Preflight(),
        GetVideoList(),
        InitialzeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]
    p = Pipeline(steps)
    p.run(user_input, utili_object)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print('the project took', end - start, 'seconds')



