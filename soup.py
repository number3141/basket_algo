from bs4 import BeautifulSoup

fileBask = open('bask.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fileBask, 'lxml')

