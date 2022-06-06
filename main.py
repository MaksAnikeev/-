import os
import urllib.parse
import requests
import argparse

from dotenv import load_dotenv

def is_bitlink(bitlink, bitly_token):
    headers = {"Authorization": f'Bearer {bitly_token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    return response.ok


def shorten_link(user_url, bitly_token):
    headers = {"Authorization": f'Bearer {bitly_token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": user_url}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(bitlink, bitly_token):
    headers = {"Authorization": f'Bearer {bitly_token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    payload = {'units': -1}
    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()
    click_score = response.json()['total_clicks']
    return click_score


if __name__ == "__main__":
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']

    parser = argparse.ArgumentParser(description='Описание что делает программа')
    parser.add_argument('user_url', help='Адрес сайта (url) или битлинк')
    args = parser.parse_args()

    parsed_user_url = urllib.parse.urlparse(args.user_url)
    bitlink = parsed_user_url.netloc + parsed_user_url.path

    if not parsed_user_url.scheme:
        full_user_url = f'https://{args.user_url}'
    else:
        full_user_url = args.user_url

    try:
        if is_bitlink(bitlink, bitly_token):
            print('Итого кликов по ссылке: ',
                  count_clicks(bitlink, bitly_token))
        else:
            print('Битлинк', shorten_link(full_user_url, bitly_token))
    except requests.exceptions.HTTPError:
        print('Некорректный адрес url или битлинк')
