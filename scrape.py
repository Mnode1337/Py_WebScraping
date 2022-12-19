from bs4 import BeautifulSoup
import requests

def main():

    source = requests.get('http://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')

    # print(soup.prettify())
    article = soup.find('article')
    print("\n")
    # print(article.prettify())

    summary = article.find('div', class_='entry-content').p.text
    # print(summary)
    video_src = article.find('iframe', class_='youtube-player')['src']
    # print(video_src)

    vid_id = video_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # print(vid_id)
    # watch = route, query parameter = ?,
    yt_link = f'https://youtube.com/watch?v={vid_id}'

    print(yt_link)

    try:
        pass
    except Exception as e:
        raise e

    '''
    headline = article.h2.a.text
    print(headline)
    '''

if __name__ == '__main__':
    main()