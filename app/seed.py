from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

#*********************************************************************************************************

sql = """
insert into delincuentes (rut,nombre,apellido_paterno,apellido_materno,edad) values
 ('190323323','bastian','lopez','orellana','23')
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
cur.execute(sql)

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('1','quilicura','me robaron en la calle, de dia cuando sali a comprar','04022018','150')
 returning id;
 """

cur.execute(sql)

#*********************************************************************************************************


sql = """
insert into delincuentes (rut,nombre,apellido_paterno,apellido_materno,edad) values
 ('189320312','camila','gonzalez','dontknow','19')
returning id;
"""
cur.execute(sql)

sql = """
insert into CARACTERISTICAS (usuario_id,sexo,estatura,contextura_fisica,
           tez_piel,nacionalidad,tono_voz,color_pelo,color_ojos,tatuajes) values
           ('2','femenino','165','atletica','blanca','chilena','aguda','cafe','negro','si')
returning id;
"""

cur.execute(sql)

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('2','laflorida','que sad es que te roben','02142014','150')
 returning id;
 """
cur.execute(sql)


#*********************************************************************************************************

sql = """
insert into delincuentes (rut,nombre,apellido_paterno,apellido_materno,edad) values
 ('1100010101','andrea','ramirez','heitcher','32')
returning id;
"""
cur.execute(sql)

sql = """
insert into CARACTERISTICAS (usuario_id,sexo,estatura,contextura_fisica,
           tez_piel,nacionalidad,tono_voz,color_pelo,color_ojos,tatuajes) values
           ('3','femenino','180','media','afroamericana','extranjera','aguda','negro','negro','no')
returning id;
"""

cur.execute(sql)

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('3','lascondes','asalto a mano armada','23012014','1200')
 returning id;
 """
cur.execute(sql)

sql = """
insert into HISTORIAL (usuario_id, sector, relato, fecha, hora) values
 ('4','lascondes','asalto a mano armada, cerca del lugar','23012014','1300')
 returning id;
 """
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
