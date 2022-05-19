import logging

class logger:
    def __init__(self):
        """
        """
       
        pass

    def my_logs(self,logmessage):
        self.logmessage = logmessage
        logging.basicConfig(filename="insurance.log",format='%(asctime)s %(message)s',filemode='a')
        logger = logging.getLogger()
        logger.warning(self.logmessage)
        return self.logmessage 

if __name__ == '__main__':
    log = logger()
    log.my_logs('hello world')