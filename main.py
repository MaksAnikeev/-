# import argparse
# import os
# import urllib.parse
#
# import requests
# from dotenv import load_dotenv
#
#
# def is_bitlink(bitlink, bitly_token):
#     headers = {"Authorization": f'Bearer {bitly_token}'}
#     url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
#     response = requests.get(url, headers=headers)
#     return response.ok
#
#
# def shorten_link(user_url, bitly_token):
#     headers = {"Authorization": f'Bearer {bitly_token}'}
#     url = 'https://api-ssl.bitly.com/v4/bitlinks'
#     payload = {"long_url": user_url}
#     response = requests.post(url, json=payload, headers=headers)
#     response.raise_for_status()
#     bitlink = response.json()['id']
#     return bitlink
#
#
# def count_clicks(bitlink, bitly_token):
#     headers = {"Authorization": f'Bearer {bitly_token}'}
#     url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
#     payload = {'units': -1}
#     response = requests.get(url, params=payload, headers=headers)
#     response.raise_for_status()
#     click_score = response.json()['total_clicks']
#     return click_score
#
#
# if __name__ == "__main__":
#     load_dotenv()
#     bitly_token = os.environ['BITLY_TOKEN']
#
#     parser = argparse.ArgumentParser(description='Описание что делает программа')
#     parser.add_argument('user_url', help='Адрес сайта (url) или битлинк')
#     args = parser.parse_args()
#
#     parsed_user_url = urllib.parse.urlparse(args.user_url)
#     bitlink = parsed_user_url.netloc + parsed_user_url.path
#
#     if not parsed_user_url.scheme:
#         full_user_url = f'https://{args.user_url}'
#     else:
#         full_user_url = args.user_url
#
#     try:
#         if is_bitlink(bitlink, bitly_token):
#             print('Итого кликов по ссылке: ',
#                   count_clicks(bitlink, bitly_token))
#         else:
#             print('Битлинк', shorten_link(full_user_url, bitly_token))
#     except requests.exceptions.HTTPError:
#         print('Некорректный адрес url или битлинк')
import os
import urllib.parse
import requests
import argparse

from dotenv import load_dotenv

parse = argparse.ArgumentParser(
    description='Описание что делает программа'
)
parse.add_argument('link', help='ссылка')
args = parse.parse_args()
user_url = args.link

load_dotenv()
token = os.environ["BITLY_TOKEN"]


def is_bitlink(bitlink, token):
    headers = {"Authorization": f'Bearer {token}'}
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=headers)
    return response.ok


def shorten_link(new_user_url, token):
    headers = {"Authorization": f'Bearer {token}'}
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {"long_url": new_user_url}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    count_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'units': -1}
    response = requests.get(count_clicks_url, headers=headers, params=payload)
    response.raise_for_status()
    click_score = response.json()['total_clicks']
    return click_score


if __name__ == "__main__":
    parsed_user_url = urllib.parse.urlparse(user_url)
    bitlink = parsed_user_url.netloc + parsed_user_url.path

    # https://bit.ly/3H9UC7R
    # link = 'https://www.google.com/search?q=rjn&oq=rjn&aqs=chrome.0.69i59j69i57j69i60l2j69i65.3247j0j7&sourceid=chrome&ie=UTF-8'
    if not parsed_user_url.scheme:
        new_user_url = f'http://{user_url}'
    else:
        new_user_url = user_url

    try:
        if is_bitlink(bitlink, token):
            click_score = count_clicks(token, bitlink)
            print('Кликов по ссылке: ', click_score)
        else:
            print('Битлинк: ', shorten_link(new_user_url, token))
    except requests.exceptions.HTTPError:
        print('неправильная ссылка')