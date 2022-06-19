from Search_Youtube_Caption.pipeline.Steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')