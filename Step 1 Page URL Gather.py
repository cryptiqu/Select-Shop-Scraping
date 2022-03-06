from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.shoppingmap.it/negozi?page=30').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ ='title desktop-only')

txt_file = open("Company URL Page Messy all.txt", "a")
txt_file.write(f'''
{jobs}
''')
txt_file.close()
