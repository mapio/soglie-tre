from re import sub
from sys import exit

from bs4 import BeautifulSoup
import requests

r0 = requests.get('http://ac3.tre.it/133/index.jsp?uri=/133/costi-e-soglie.jsp')
try:
	session_id = r0.cookies['JSESSIONID']
except KeyError:
	exit('soglie_tre: errore di esecuzione, potresti non essere sotto rete Tre')
r1 = requests.get('http://ac3.tre.it/133/costi-e-soglie.jsp', cookies = {'device': 'mobile-evo', 'JSESSIONID': session_id})

soup = BeautifulSoup(r1.text, 'html.parser')
try:
	notes = soup.find_all('div', 'box_Note')
except ValueError:
	exit('soglie_tre: errore di esecuzione, potresti non essere sotto rete Tre')

def clean(e):
	return sub( r'<[^>]+>', '', u' '.join(map(lambda _: unicode(_).strip(), e.contents)))

for note in notes:
	print clean(note)
