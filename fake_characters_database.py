# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:51:56 2020

@author: mam22
"""

import mysql.connector
import json

with open('database.json') as json_data_file:
    database_config = json.load(json_data_file)

connection = mysql.connector.connect(host=database_config['host'],user=database_config['user'],passwd=database_config['password'],database=database_config['database'])
cursor = connection.cursor()

with open('fake-characters.txt') as f:
    fake_anime_characters = f.read()

fake_anime_characters = fake_anime_characters.split('\n')
fake_anime_characters = [(name,) for name in fake_anime_characters]
cursor.executemany("""
               INSERT INTO FAKE_ANIME_CHARACTER(NAME) VALUES (%s)
               """,fake_anime_characters)
connection.commit()
