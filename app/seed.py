from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql = """
insert into DELNCUENTES (rut,nombre,apellido_paterno,apellido_materno,edad) values
 ('190323323','bastian,'lopez','orellana','23')
returning id;
"""
cur.execute(sql)

sql = """
insert into CARACTERISTICAS (usuario_id,sexo,estatura,contextura_fisica,
           tez_piel,nacionalidad,tono_voz,color_pelo,color_ojos,tatuajes) values
           ('1','masculino','183','atletica','morena','chilena','grave','negro','negro','no')
returning id;
"""

cur.execute(sql)

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('1','vitacura','MME ROBARRRON EN LA CALLEEE','03022018','1650')
 returning id;
 """

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('1','quilicura','MME ROBARRRON EN LA CALLEEE denuvo','04022018','150')
 returning id;
 """

cur.execute(sql)

conn.commit()
cur.close()
conn.close()
