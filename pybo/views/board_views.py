from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def board_list(request):
    ''' bootstrap template'''
    return render(request, 'pybo/board_list.html')
