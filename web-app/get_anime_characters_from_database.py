# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:28:44 2020

@author: mam22
"""

import mysql.connector
import json
import random
def reverse_first_and_last_name(name):
    names = name.split(',')
    if(len(names) == 2):
        return names[1].strip()+" "+names[0].strip()
    else:
        return names[0].strip()

with open('../database.json') as json_data_file:
    database_config = json.load(json_data_file)

def get_anime_characters_for_quiz():
    connection = mysql.connector.connect(host=database_config['host'],user=database_config['user'],passwd=database_config['password'],database=database_config['database'])
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT NAME from ANIME_CHARACTER")
    characters = cursor.fetchall()
    real_anime_characters=[(reverse_first_and_last_name(character[0]),True) for character in characters]
    cursor.execute("SELECT NAME from FAKE_ANIME_CHARACTER")
    fake_characters = cursor.fetchall()
    fake_anime_characters=[(character[0],False) for character in fake_characters]
    
    real_anime_characters_sample = random.sample(real_anime_characters,len(real_anime_characters)//2)
    fake_anime_characters_sample = random.sample(fake_anime_characters,len(fake_anime_characters)//2)
    
    all_anime_characters=[]
    all_anime_characters.extend(real_anime_characters_sample)
    all_anime_characters.extend(fake_anime_characters_sample)
    random.shuffle(all_anime_characters)
    connection.close()
    return all_anime_characters



