from os import path
from winshell import desktop

from requests import get
from bs4 import BeautifulSoup
from webbrowser import open as open_url

def main():
    url = 'https://adultmult.club/'
    request = get(url)

    if request.status_code != 200:
        raise Exception(f'Something went wrong, response code is {request.status_code}')

    content = request.text
    soup = BeautifulSoup(content, 'lxml')
    parent = soup.find('ul', id='gallery-3c')

    mirrors = []

    for a in parent.find_all('a', href=True):
        if 'Зеркало' in (a.text):
            mirrors.append(a['href'])

    open_url(mirrors[0], new=0)

    for index, mirror in enumerate(mirrors, start=1):
        shortcut_path = path.join(
            desktop(),
            f'adultmult{index}.url'
        )

        with open(shortcut_path, 'w') as shortcut:
            shortcut.write('[InternetShortcut]\n')
            shortcut.write(f'URL={mirror}')

if __name__ == '__main__':
    main()
