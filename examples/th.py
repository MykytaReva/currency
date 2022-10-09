from concurrent import futures
from multiprocessing import Process

import requests
from time import sleep, time
from threading import Thread, current_thread

def foo(b):
    print(f'START{ current_thread()}')
    sleep(b)
    print(f'END  { current_thread()}')
start = time()

# URLS = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BA%D1%96%D0%BF%D0%B5%D0%B4%D1%96%D1%8F:%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BB_%D1%81%D0%BF%D1%96%D0%BB%D1%8C%D0%BD%D0%BE%D1%82%D0%B8',
#     'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8',
#     'https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:LintErrors',
# ] * 40
#
# def requests_get(url):
#     response = requests.get(url)
#     print(response.status_code)
#
# with futures.ThreadPoolExecutor(10) as executor:
#     threads = []
#     for url in URLS:
#         threads.append(executor.submit(requests_get, url=url))
#
#     for th in threads:
#         th.result()


def countdown(n):
    while n != 0:
        n -= 1
n = 500_000_000

th1 = Process(target=countdown, args=[n//2])
th2 = Process(target=countdown, args=[n//2])
th1.start()
th2.start()
th1.join()
th2.join()

end = time()
print(f'took time {end - start}')