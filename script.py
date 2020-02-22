import requests
from bs4 import BeautifulSoup as bs
import mysql.connector

headers = {
    'Authorization': 'Token 3ab9e0f27b8200c9c170f5e2963097c24c30a4d6',
    'Content-Type': 'application/json',
}

params = (
    ('institution', 'Lviv Polytechnic National University, LPNU'),
)
def Insertion_to_Database(publishing_name, id, rid, url, api, publications):
    try:
        connection = mysql.connector.connect(user = 'root', password = 'toor', host = 'localhost', database = 'professors', charset='utf8')
        cursor = connection.cursor(buffered=True)
        Insertion_Query = """INSERT INTO professor(publishing_name, id, rid, url, api, publications)
                             VALUES(%s, %s, %s, %s, %s, %s)"""
        Values_to_Insert = (publishing_name, id, rid, url, api, publications)
        cursor.execute(Insertion_Query, Values_to_Insert)
        connection.commit()
        print("Professor ", publishing_name, " was inserted!")
       
    except  mysql.connector.Error as error:
        print("Failed to insert successfully into professor table{}".format(error))
        print(publishing_name)

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()


response = requests.get('https://publons.com/api/v2/academic/', headers=headers, params=params).json()
count = 0
for j in response['results']:
    publishing_name_u = j['publishing_name'].encode().decode()
    Insertion_to_Database(publishing_name_u,j['ids']['id'], j['ids']['rid'],
                        j['ids']['url'], j['ids']['api'], j['publications']['url'])
    count += 1
print(count)
while(response['next'] != None):
    response = requests.get(response['next'], headers=headers).json()
    for j in response['results']:
        """ for i in j:
            print(i)
            print(j[i]) 
         """
        Insertion_to_Database(j['publishing_name'],j['ids']['id'], j['ids']['rid'],
                        j['ids']['url'], j['ids']['api'], j['publications']['url'])
        
        count += 1
    print(count)
        
    