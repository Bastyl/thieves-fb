from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)

sql ="""
CREATE TABLE test 
           (id serial PRIMARY KEY, num integer, data varchar);
"""

cur.execute(sql)

conn.commit()
cur.close()
conn.close()