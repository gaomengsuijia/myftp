#coding:utf-8
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = "%s\data"%BASE_DIR
FILE_DIR = "%s\file_data"%BASE_DIR
print(DATA_DIR)
sys.path.append(BASE_DIR)
#login flag
