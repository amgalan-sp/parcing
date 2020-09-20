from making_folder import make_dir_for_images
from download import download_book
from bs4_tutorial import get_title
import os
import requests

foldername = 'books'
try:
	os.makedirs(foldername, exist_ok=True)
	print("Directory '%s' created successfully" %foldername) 
except OSError as error: 
    print("Directory '%s' can not be created")

filepath = os.path.join(os.getcwd(), foldername)
os.chdir(filepath)
for id in range(1, 11):
    #url = 'http://tululu.org/txt.php?id={}'.format(id)
    url = 'http://tululu.org/b{}'.format(id)
    try:
        print('Заголовок: ', get_title(url)[0])
        print('Автор: ', get_title(url)[3])
    except AttributeError:
        pass
    #filename = 'book{}'.format(id)
    #download_book(url, filename)