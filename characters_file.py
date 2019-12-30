# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:53:26 2019

@author: mam22
"""

import mysql.connector

def reverse_first_and_last_name(name):
    names = name.split(',')
    if(len(names) == 2):
        return names[1].strip()+" "+names[0].strip()
    else:
        return names[0].strip()

connection = mysql.connector.connect(host='localhost',user='root',passwd='mysql',database='anime_schema')

cursor = connection.cursor()

cursor.execute("SELECT DISTINCT NAME from ANIME_CHARACTER")
characters = cursor.fetchall()
file = open("characters.txt","w",encoding='utf-8')
for character in characters:
    print(character[0])
    file.write(reverse_first_and_last_name(character[0])+"\n")