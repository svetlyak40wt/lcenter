#!env/bin/python

import requests
import click

from lxml.html import fromstring

def process_doctor(url):
    headers = {'Cookie': 'beget=begetok'}
    response = requests.get(url, headers=headers)

    data = fromstring(response.text)

    title = data.xpath('//*[@id="page-title"]/text()')
    print(title[0])

    cells = data.xpath('//*[@id="doctors-timetable"]/ul/li')
    free_cells = [cell
                  for cell in cells
                  if 'busy-date' not in set(cell.classes)]

    if free_cells:
        for cell in free_cells:
            print('  ' + cell.text)
    else:
        print('  нет свободного времени на сегодня')



@click.command()
@click.argument('url', nargs=-1)
def main(url):
    for who in url:
        process_doctor(who)


if __name__ == '__main__':
    main()
