# Get the covid statewise data as desktop notification

from socket import timeout
from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\songs\covid.ico",
        timeout = 20
    )

def getData(url):
    r = requests.get(url)
    return r.text



if __name__ == "__main__":
    # notifyMe(" Deblina "," Let's stop the spread of Omicron! ")
    myHtmlData = getData('https://dmerharyana.org/omicron-cases-in-india-today/')
    #print(myHtmlData)

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.prettify())

    myDataStr =""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]    
    itemlist = myDataStr.split("\n\n")

    states =['Gujarat','West Bengal']
    for item in itemlist[0:21]:
        dataList = item.split('\n')
        if dataList[1] in states:
            print(dataList)


            nTitle = 'Covid Cases'
            ntext = f"{dataList[1]}:{dataList[2]}"
            notifyMe(nTitle,ntext)