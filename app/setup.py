from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""DROP TABLE DELINCUENTES;
        DROP TABLE CARACTERISTICAS;
        DROP TABLE HISTORIAL;
        DROP TABLE SECTOR;


"""

cur.execute(sql)

sql ="""
CREATE TABLE DELINCUENTES 
           (id serial PRIMARY KEY, rut integer, nombre varchar, apellido_paterno varchar, apellido_materno varchar, edad integer);
CREATE TABLE CARACTERISTICAS 
           (id serial PRIMARY KEY, usuario_id integer, sexo varchar, estatura_min integer, estatura_max integer, contextura_fisica varchar,
           tez_piel varchar, nacionalidad varchar, tono_voz varchar,color_pelo varchar,color_ojos varchar,tatuajes varchar);
CREATE TABLE HISTORIAL 
           (id serial PRIMARY KEY, usuario_id integer, sector_id integer, relato var_char, fecha integer, hora integer);
CREATE TABLE SECTOR 
           (id serial PRIMARY KEY, zona varchar, lugar_fisico varchar);
"""



cur.execute(sql)
conn.commit()
cur.close()
conn.close()
