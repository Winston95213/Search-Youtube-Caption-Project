from Search_Youtube_Caption.pipeline.Steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()
