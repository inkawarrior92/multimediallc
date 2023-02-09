import inspect
import logging
import os
from datetime import date


def customLogger(logLevel=logging.DEBUG):

    # gets name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    # loggerName refers to the method that will be logged
    logger = logging.getLogger(loggerName)
    # by default log all messages
    logger.setLevel(logging.DEBUG)


    today = date.today()
    day = today.strftime("%m-%d-%y")
    #filename = os.getcwd() + "/automation" + str(day) + ".log"
    filename = "automation" + str(day) + ".log"
    logDir = "../logs/"
    relativeFileName = logDir + filename
    currentDir = os.path.dirname(__file__)
    destinationFile = os.path.join(currentDir, relativeFileName)
    destinationDir = os.path.join(currentDir, logDir)
    if not os.path.exists(destinationDir):
        os.makedirs(destinationDir)

    # {0}.log will generate multiple log files instead of one automation.log
    # mode = a to append files, if w, and having multiple files will write new files
    fileHandler = logging.FileHandler(destinationFile, mode="a")
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s",
                                  datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
