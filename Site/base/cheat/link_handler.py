import requests


def stream_validator(link):
    try:
        rq = requests.request(method='GET', url=link)
        return rq.status_code == 200
    except Exception:
        return False



# Функция меняет обычную ссылку на стрим на ссылку для i-frame'a
def transformate(old_link: str):
    new_link = old_link.replace('https://www.youtube.com/live/', 'https://www.youtube.com/embed/')
    return new_link
