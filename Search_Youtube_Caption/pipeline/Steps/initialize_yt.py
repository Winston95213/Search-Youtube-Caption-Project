from .step import Step
from Search_Youtube_Caption.model.yt import YT


class InitialzeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]