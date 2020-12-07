import requests
from bs4 import BeautifulSoup
from noti import send


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def c19_bot():

    url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
    soup = create_soup(url)

    c19_info = soup.find("tbody").find_all("tr")

    c19_dict = {}
    for c19 in c19_info:
        c19_area = c19.find("th").text
        c19_sum = c19.find_all("td")[0].text
        c19_domestic = c19.find_all("td")[1].text
        c19_overseas = c19.find_all("td")[2].text
        
        if c19_area == "합계" or c19_area == "대전" or c19_area == "충북":    
            c19_dict[c19_area] = [c19_sum, c19_domestic, c19_overseas]

    for k, v in c19_dict.items():
        print("-"*10 + f"{k}" + "-"*10)
        print(f"합계 : {v[0]},  국내발생 : {v[1]}, 해외발생 : {v[2]}")
        print()




if __name__ == "__main__":
    send(c19_bot())   # 코로나 지역, 합계, 국내발생, 해외발생

