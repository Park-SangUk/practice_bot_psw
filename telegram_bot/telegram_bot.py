import requests
from bs4 import BeautifulSoup
from noti import send
import telegram

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def c19_bot():

    url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
    soup = create_soup(url)

    results = []
    c19_infos = soup.find("tbody").find_all("tr")
    for c19_info in c19_infos:
        area = c19_info.find("th").text
        if area == "합계" or area == "대전" or area == "충북":
            c19_status = c19_info.find_all("td", limit=3)
            for c19 in c19_status:
                results.append(c19.text)
    
    return results


if __name__ == "__main__":
    send(c19_bot())   # 코로나 지역, 합계, 국내발생, 해외발생

