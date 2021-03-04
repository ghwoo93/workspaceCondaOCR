from PIL import Image       #pip install pillow
from pytesseract import *   #pip install pytesseract
import configparser
import os

#Config Parser 초기화
config = configparser.ConfigParser()
#Config File 읽기
