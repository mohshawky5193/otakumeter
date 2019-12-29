# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class AnimeInfoExtractionPipeline(object):
    def __init__(self):
        self._create_connection()
    def _create_connection(self):
        host='localhost'
        user='root'
        password='mysql'
        db='anime_schema'
        self.connection = mysql.connector.connect(host=host,user=user,passwd=password,database=db)
        self.cursor = self.connection.cursor()
    
    def _insert_item(self,item):
        
        try:
            self.cursor.execute("""
                                INSERT INTO ANIME VALUES(%s,%s)
                                """,(item['anime_id'],item['anime_name']))
            self.connection.commit()
            if(len(item['character_names']) > 0):
               for character in item['character_names']:
                   self.cursor.execute("""
                                INSERT INTO ANIME_CHARACTER (NAME,ANIME_ID) VALUES(%s,%s)
                                """,(character,item['anime_id']))
                   self.connection.commit()
        except mysql.connector.Error as err:
            print('Database Error {}'.format(err))
            self.connection.rollback()
    def process_item(self, item, spider):
        self._insert_item(item)
        return item
