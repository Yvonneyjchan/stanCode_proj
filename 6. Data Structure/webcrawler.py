"""
File: webcrawler.py
Name: Yvonne Chan
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.tbody.find_all('tr')  # 直接對 soup 裡面的 <tbody> 物件 取出文字

        male = 0
        female = 0

        rank = 0

        for tag in tags:
            rank += 1
            if rank <= 200:
                td = tag.find_all('td')
                male += int(string_manipulation(td[2].text))
                female += int(string_manipulation(td[4].text))
        print('Male Number: ', male)
        print('Female Number: ', female)


def string_manipulation(s):
    ans = ''
    for ch in s:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()
