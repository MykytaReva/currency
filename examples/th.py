import logging
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# logging.basicConfig(filename='app.log',
#                     filemode='a',
#                     format='%(asctime)s - %(message)s', level=logging.INFO,
#                     datefmt='%d-%b-%y %H:%M:%S')
# logging.critical('Admin logged in')
# Create a custom logger
# logger = logging.getLogger(__name__)
#
# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)
#
# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
#
# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
#
# logger.warning('This is a warning')
# logger.error('This is an error')

#
# import requests
#
# # response = requests.options('https://api.privatbank.ua/p24api/exchange_rates?json&date=15.10.2022')
# # print(response)
#
# # headers = {'content-type': 'application/json'}
# params = {'json': None, 'date': '15.10.2022'}
# params = '&'.join([k if v is None else f"{k}={v}" for k, v in params.items()])
# response = requests.get('https://api.privatbank.ua/p24api/exchange_rates',
#             params=params)
# print(response.url)

