import os
import psycopg2 as pg

class Banco:
    def __init__(self, user, passwd, dbname, pg_host, pg_port ):
        self.user = user
        self.passwd = passwd
        self.dbname = dbname
        self.pg_host = pg_host
        self.pg_port = pg_port
        self.url_connection = "user="+  self.user+ " password="+ self.passwd + " host="+ self.pg_host + " port="+ self.pg_port + " dbname="+dbname
    
    def execute_query(self, query):
        postgres = pg.connect(self.url_connection) 
        postgres.autocommit = True
        select = postgres.cursor()
        select.execute(query)
        postgres.close()

    def select_query(self, query):
        postgres = pg.connect(self.url_connection) 
        postgres.autocommit = True
        select = postgres.cursor()
        select.execute(query)
        result = select.fetchall()
        postgres.close()
        return result