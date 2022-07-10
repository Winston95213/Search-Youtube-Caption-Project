import logging

from Search_Youtube_Caption.pipeline.Steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger = logging.getLogger('Logger')
        logger.info("Preflight: Creating Directory...")
        utils.create_dirs()
