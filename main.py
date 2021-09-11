import time
import logging
import multiprocessing
import concurrent.futures
from threading import Thread
from json import JSONDecoder

cores = multiprocessing.cpu_count()

def hola_mundo():
    print("Hola Mundo")
    #time.sleep(5)

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == '__main__':
    #for i in range(cores):
    #    thread = Thread(target=hola_mundo)
    #    thread.start()
        #print("Adios Mundo")
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
        executor.map(thread_function, range(cores))
