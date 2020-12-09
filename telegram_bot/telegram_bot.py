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

    result = f"{date}\n"
    c19_infos = soup.find("tbody").find_all("tr")
    for c19_info in c19_infos:
        area = c19_info.find("th").text
        if area == "합계" or area == "대전" or area == "충북":
            c19_sum = c19_info.find("td", attrs={"headers": "status_level l_type1"}).text
            c19_1 = c19_info.find("td", attrs={"headers": "status_level l_type2"}).text
            c19_2= c19_info.find("td", attrs={"headers": "status_level l_type3"}).text
            result = result + f"---------- {area} ----------\n총 발생: {c19_sum}\n국내발생 : {c19_1}\n해외유입 : {c19_2}\n"
    return result


if __name__ == "__main__":
    send(c19_bot())   # 코로나 지역, 합계, 국내발생, 해외발생

