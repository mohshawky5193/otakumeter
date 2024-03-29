# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
import json

with open('../../database.json') as json_data_file:
    database_config = json.load(json_data_file)
class AnimeInfoExtractionPipeline(object):
    def __init__(self):
        self._create_connection()
    def _create_connection(self):
        host=database_config['host']
        user=database_config['user']
        password=database_config['password']
        db=database_config['database']
        self.connection = mysql.connector.connect(host=host,user=user,passwd=password,database=db)
        self.cursor = self.connection.cursor()
    
    def _insert_item(self,item):
        
        try:
            self.cursor.execute("""
                                INSERT INTO ANIME VALUES(%s,%s)
                                """,(item['anime_id'],item['anime_name']))
            self.connection.commit()
            if(len(item['character_names']) > 0):
               for i,character in enumerate(item['character_names']):
                   id = int(item['id'][i].split('/')[4])
                   self.cursor.execute("""
                                INSERT INTO ANIME_CHARACTER (ID,NAME,ANIME_ID) VALUES(%s,%s,%s)
                                """,(id,character,item['anime_id']))
                   self.connection.commit()
        except mysql.connector.Error as err:
            print('Database Error {}'.format(err))
            self.connection.rollback()
    def process_item(self, item, spider):
        self._insert_item(item)
        #self.connection.close()
        return item
