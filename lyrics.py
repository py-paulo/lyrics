import urllib.request

from bs4 import BeautifulSoup


uri_base = 'http://www.google.com/search?q='
artist = 'Milton Nascimento'
music = 'Clube da Esquina n 2'

query_quote = ('%s %s letra' % (artist, music)).replace(' ', '+')

req = urllib.request.Request(uri_base+query_quote, headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,applica'
              'tion/signed-exchange;v=b3;q=0.9',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.google.com/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/'
                  '537.36'
})
# with urllib.request.urlopen(req) as response:
#     html = response.read().decode('utf-8', errors='ignore')

# with open('html.music.example.html', 'w') as fp:
#     fp.write(html)

with open('html.music.example.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for sub_soup in soup.find_all('div'):
    if 'data-lyricid' in sub_soup.attrs:
        for index, div in enumerate(sub_soup):
            next_div = div.find_next()
            spans = next_div.find_all('span')
            for span in spans:
                print(span.text)
        break
