from time import time
from threading import Lock
from asyncio import sleep
from datetime import datetime


class Ratelimiter:
    def __init__(self, maxRequests: int = 60):
        self.currentSecond: int = int(time())
        self.currentMinute: int = datetime.now().minute
        self.maxRequestsASecond: int = int(maxRequests * .05) if int(maxRequests * .05) >= 1 else 1
        self.maxRequestsAMinute: int = maxRequests
        self.requestsThisSecond: int = 0
        self.requestsThisMinute: int = 0
        self.threadLock = Lock()

    def __check_minute__(self):
        if self.currentMinute != datetime.now().minute:
            self.currentMinute = datetime.now().minute

    def __check_seconds__(self):
        if self.currentSecond != int(time()):
            self.currentSecond = int(time())

    async def execute(self):
        with self.threadLock:
            self.__check_minute__()
            self.__check_seconds__()
    
            if self.requestsThisSecond >= self.maxRequestsASecond:
                print(f"[RATELIMITER] Max Requests Per Second Reached ({self.requestsThisSecond}/{self.maxRequestsASecond}). Waiting...")
                while self.currentSecond == int(time()):
                    self.__check_seconds__()
                    await sleep(0.001)
                self.requestsThisSecond = 0
                print(f"[RATELIMITER] Max Requests Per Second Reset ({self.requestsThisSecond}/{self.maxRequestsASecond}). Continuing...")
    
            if self.requestsThisMinute >= self.maxRequestsAMinute:
                print(f"[RATELIMITER] Max Requests Per Minute Reset ({self.requestsThisMinute}/{self.maxRequestsAMinute}). Waiting...")
                while self.currentMinute == datetime.now().minute:
                    self.__check_minute__()
                    await sleep(0.001)
                self.requestsThisMinute = 0
                print(f"[RATELIMITER] Max Requests Per Minute Reset ({self.requestsThisMinute}/{self.maxRequestsAMinute}). Continuing...")
    
            self.requestsThisSecond += 1
            self.requestsThisMinute += 1



        