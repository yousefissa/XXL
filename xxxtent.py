import requests
url = 'http://freshman.xxlmag.com/10th-spot/?2017'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


def main(limit):
    for i in range(1, limit):
        payload = {
            'action':'media_poll_vote',
            'poll_id': 9701059,
            'post_id':232,
            'answer_id':44359115
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} votes.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
