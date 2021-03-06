import requests
from bs4 import BeautifulSoup
from noti import send
import telegram
import datetime

def create_date():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def c19_bot():

    url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
    soup = create_soup(url)
    date = create_date()

    result = f"{date} 코로나 현황\n[총발생 (국내발생 / 해외유입)]\n(매일 오전 10시 이후에 알려드립니다.)\n"
    c19_infos = soup.find("tbody").find_all("tr")
    for c19_info in c19_infos:
        area = c19_info.find("th").text
        c19_sum = c19_info.find("td", attrs={"headers": "status_level l_type1"}).text
        if c19_sum == 0:
            continue
        c19_1 = c19_info.find("td", attrs={"headers": "status_level l_type2"}).text
        c19_2= c19_info.find("td", attrs={"headers": "status_level l_type3"}).text
        result = result + f"-{area} : {c19_sum} ({c19_1} / {c19_2})\n"
    return result


if __name__ == "__main__":
    send(c19_bot())   # 코로나 지역, 합계, 국내발생, 해외발생

