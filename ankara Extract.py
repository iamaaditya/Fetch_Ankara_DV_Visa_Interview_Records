# prakash@aaditya.info
# 21 Nov 2013

import os
from urllib.request import urlopen
urlHandler = urlopen("http://www.usemb-ankara.org.tr/consular/english/schedule_dv.html")
html = str(urlHandler.read())

posRow = 0
exisList = []

##fout = open('AsiaRecords.csv', 'w+')
if os.path.exists("AsiaRecords.csv"):
    fout = open("AsiaRecords.csv", "r+")
    for currRecord in fout:
        tempval =  currRecord.split(",")
        exisList.append(tempval[0])
    ##print(exisList)
else:
    fout = open("AsiaRecords.csv", "w")

##print(exisList)

posRow = html.find('Interview Date')
valList = []
while(posRow >= 0):
    #print("Before:",posRow)
    posRow = html.find('1px">', posRow+1)
    #print("After:",posRow)
    posEnd = html.find('td', posRow)
    #print("PosEnd:",posEnd)
    if(posRow >=0):
        vall = (html[posRow+5:posEnd-2])
        vall = vall.strip()
        valList.append(vall)


for i in range(0,len(valList)-2,3):

    posAS = valList[i].find('AS')
    if( posAS < 0):
        continue
    caseNum = valList[i][posAS+2:]
    caseDate = valList[i+2][4:].strip()
    stringOut = caseNum
    stringOut += ","
    stringOut += caseDate
    stringOut += "\n"
    if(caseNum not in exisList):
        fout.write(stringOut)
        print(caseNum + ",")


fout.close()
fin.close()
