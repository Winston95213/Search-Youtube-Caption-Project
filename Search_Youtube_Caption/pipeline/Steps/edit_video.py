import logging

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        logger = logging.getLogger('Logger')
        invalid_clips = ["-nXsfXtTacE", "vUfbJH5GfuU", "2Aq_2qKn44g", "QWdhNKMZ1DI", "BPpFOM41DvY", "b9dWgUlMb9o", "1gHN-iY0KUc"]
        for found in data:
            if found.yt.id in invalid_clips:
                continue
            logger.info("Video: " +  found.yt.id)
            logger.info(self.parse_caption_time(found.time))
            start, end = self.parse_caption_time(found.time)
            try:
                video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
                clips.append(video)
            except ValueError as VE:
                logger.debug(VE)
            if len(clips) >= inputs['limit']:
                break
        logger.info(clips)

        final_clip = concatenate_videoclips(clips)
        channel_id, search_word = inputs['channel_id'], inputs['search_word']
        final_clip.write_videofile(utils.get_output_filepath(channel_id, search_word), temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000
