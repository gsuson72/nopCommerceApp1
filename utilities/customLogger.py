import logging

class LogGen:
    @staticmethod
    def loggen():
        log_format = "%(asctime)s: %(levelname)s: %(message)s"
        date_format = "%m/%d/%Y %I:%M:%S %p"
            # new version has force=True
        #for handler in logging.root.handlers[:]:
        #   logging.root.removeHandler(handler)

        logging.basicConfig(filename='.\\Logs\\automation.log', filemode="a", force=True,
                            format=log_format, datefmt=date_format)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

