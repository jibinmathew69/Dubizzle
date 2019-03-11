'''
A better approach wuld be to use asyncio or celery to asynchronously fetch the urls coordinated using semaphore to
limited the number of parallel requests, however the evaluating compiler doesn't seem to support the libraries.
'''
import urllib.request
import json


def fetcher(substr,page):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=%s&page=%s"
    query = url%(substr,page)
    try:
        with urllib.request.urlopen(query) as url:
            response = json.loads(url.read().decode())
    except:
        return None

    return response

def getMovieTitles(substr):
    titles = []

    #first fetch for metadata and data
    resp = fetcher(substr,1)
    if resp is None:
        return []

    [titles.append(dic['Title']) for dic in resp['data']]

    for i in range(2,resp['total_pages']+1):
        response = fetcher(substr,i)
        [titles.append(dic['Title']) for dic in response['data']]

    return sorted(titles)


print(get_movie_titles('spiderman'))