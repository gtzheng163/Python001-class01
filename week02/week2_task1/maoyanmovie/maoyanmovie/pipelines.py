# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import pymysql.cursors
from scrapy.exporters import CsvItemExporter


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '12345678',
    'charset' : 'utf8',
    'db' : 'pytestdb'
}


# Connect to the database
connection = pymysql.connect(host=dbInfo['host'],
                             port=dbInfo['port'],
                             user=dbInfo['user'],
                             password=dbInfo['password'],
                             db=dbInfo['db'],
                             charset=dbInfo['charset'],
                             cursorclass=pymysql.cursors.DictCursor)

cursor = None

class MaoyanProPipeline:

    def open_spider(self, spider):
        global cursor
        cursor = connection.cursor()


    def process_item(self, item, spider):
        global cursor
        movie_name = item['title']
        movie_type = item['movie_type']
        play_date = item['release_date']

        try:
            sql = "INSERT INTO `movie_info` (`title`, `movie_type`, `release_date`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (title, movie_type, release_date))
        except:
            cursor.rollback()

        return item

    def close_spider(self, spider):
        cursor.close()
        connection.commit()
        connection.close()
