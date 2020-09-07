#-*-coding:utf-8-*-
import corona
import time


if __name__ == '__main__':
    corona_json = corona.corona()

    while(True):
        corona_json._get_movement()
        time.sleep(400)
    