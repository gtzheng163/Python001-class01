
# 作业一：
# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'Cookie':'__mta=246659387.1593254587112.1593260532714.1593263169886.6; uuid_n_v=v1; uuid=FA9DC1D0B86211EA974289B279A7041D22A68D6FCB1F45C5952698F6B08F0D7D; _csrf=d89f138989c612f67ccd3b8ad427d180a3b409ddb95a2851d7659dc73793ee59; __guid=17099173.2277230876625161500.1593254585167.3857; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593254586; _lxsdk_cuid=172f55fa6bac8-0ca9aac12ca2b7-376b4502-1fa400-172f55fa6ba61; _lxsdk=FA9DC1D0B86211EA974289B279A7041D22A68D6FCB1F45C5952698F6B08F0D7D; mojo-uuid=a7f6d5ff42ee1ddd78c9a908527e08a9; monitor_count=9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593268192; mojo-session-id={"id":"c3a6d968547576553996e89b6aefeaff","time":1593268191781}; mojo-trace-id=1; __mta=246659387.1593254587112.1593263169886.1593268191881.7; _lxsdk_s=172f62f424d-e39-f70-b37%7C%7C2',
          'user-agent': user_agent}

url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)

bs_info = bs(response.text, 'html.parser')

movie_details = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    name = tags.find('span', attrs={'class': 'name'}).text
    scores = tags.find('span', attrs={'class': 'score channel-detail-orange'})
    if scores is not None:
        integer = scores.find('i', attrs={'class': 'integer'}).text
        fraction = scores.find('i', attrs={'class': 'fraction'}).text
        movie_score = integer+fraction
    else:
        movie_score = '暂无评分'
    for divs in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        for spans in divs.find_all('span', attrs={'class': 'hover-tag'}):
            if spans.text == '类型:':
                spans.replace_with('')
                movie_type = divs.text.replace(' ', '').strip()
    movie_detail = [name, movie_score, movie_type]
    movie_details.append(movie_detail)

maoyan_top10 = pd.DataFrame(data=movie_details[:10])

maoyan_top10.to_csv('D:/Python Venv/learn/maoyan_top10.csv', encoding='utf-8', index=False, header=['影片名称', '评分', '种类'])