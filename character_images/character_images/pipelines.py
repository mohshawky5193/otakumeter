# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import mysql.connector
import json

with open('../../database.json') as json_data_file:
    database_config = json.load(json_data_file)

class CharacterImagesPipeline(object):
    def __init__(self):
        self._create_connection()
    def _create_connection(self):
        host=database_config['host']
        user=database_config['user']
        password=database_config['password']
        db=database_config['database']
        self.connection = mysql.connector.connect(host=host,user=user,passwd=password,database=db)
        self.cursor = self.connection.cursor()
    
    def _update_link(self,item):
        
        try:
            self.cursor.execute("""
                                UPDATE ANIME_CHARACTER SET CHARACTER_IMAGE_URL = %s where ID = %s
                                """,(item['character_image_link'][0],item['character_id']))
            self.connection.commit()
        except mysql.connector.Error as err:
            print('Database Error {}'.format(err))
            self.connection.rollback()
    def process_item(self, item, spider):
        self._update_link(item)
		#self.connection.close()
        return item
