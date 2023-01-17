import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='a',
                    format='%(asctime)s %(filename)s %(name)s - %(levelname)s - %(message)s')



