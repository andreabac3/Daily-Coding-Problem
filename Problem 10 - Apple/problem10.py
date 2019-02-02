#!/usr/bin/env python3
from time import sleep
from threading import Thread

def solve(function, ms):
    sleep(ms/1000.0)
    function()

def printHello():
    print("Hello")



if __name__ == "__main__":
    n = 5000
    thread = Thread(target = solve(printHello, n))
    thread.start()
