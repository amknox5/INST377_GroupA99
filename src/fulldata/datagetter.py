import requests
from os import path
import csv
##
def filemaker(heads,jsn,name,i):
    with open("data/"+ name + i + 'DataSet.csv', 'w',errors = 'IGNORE',newline='') as file:
        writer = csv.DictWriter(file, fieldnames = heads)
        writer.writeheader()
        writer.writerow(jsm)
        file.close
#-------------------------#
def heads(support):
    ids = []
    with open(support,"r") as file:
        data = csv.DictReader(file)
        for i in data:
            heads = [j for j in i.keys()]
            break
        for i in data:
            ids.append(i[heads[0]])
    return ids
#---------------------------#
def headfind(jsn):
    headers = []
    for i in jsn:
        headers.append(i)
    return headers
#---------------------------#
def dataget(helper,name,ids,extra,headers):
    fulljson = []
    for i in ids:
        out=requests.get(helper[name.upper()] + i + extra)
        jsn = out.json()
        filemaker(headers,jsn,name,i)
    ##newfile(headers,fulljson,name)
#---------------------------#
def maker(helper,name):
    extra = ""
    if name.upper() == "STOPID":
        support = "data\stopsDataSet.csv"
    elif name.upper() == "ROUTES":
        support = "data/busesDataSet.csv"
    else:
        support = "data/busesDataSet.csv"
        extra = "/schedules"
    ids = heads(support)
    for i in ids:
        out=requests.get(helper[name.upper()] + i + extra)
        newj = out.json()
        break
    headers = headfind(newj)
    dataget(helper,name,ids,extra,headers)
#----------------------------#
def main():
    helper = {'STOPID':'https://api.umd.io/v1/bus/stops/',
              'ROUTES':'https://api.umd.io/v1/bus/routes/',
              'TIMES':'https://api.umd.io/v1/bus/routes/'}
    for i in helper.keys():
        print(i)
    inner = input("What API data would you like to Put (From above): ")
    if inner.upper() in helper.keys():
        if path.exists("data/"+inner + "DataSet.csv") == True: 
            cho = input("This Data Set has already been made would you like to update it? (y/n): ")
            if cho.rstrip().upper() == "Y":
                maker(helper,inner)
        else:
            maker(helper,inner)
    else:
        retyp = input("That input was not correct would you like to try again? (y/n): ")
        if retyp.rstrip().upper() == "Y":
            main()
    print("Done")
#--------------------------------#
if __name__ == "__main__":
    main()