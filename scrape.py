from bs4 import BeautifulSoup
import requests

def main():

    with open('simple.html') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        # print(soup.prettify())
    match = soup.title.text
    print("\n")
    print(match)

if __name__ == '__main__':
    main()