import sqlite3

def get_db_connection():
   conn = sqlite3.connect('datubaze.SQLite')
   return conn



def izveidot_tabulu():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE TERMINS (ID serial, Name varchar (50))
    """)
    conn.commit()
    cur.close()
    conn.close()
    return



def ieraksta(lietotajvards):
  conn = get_db_connection()
  conn.execute(
    """
      INSERT INTO TERMINS (Name)
      VALUES ('{}')""".format(lietotajvards))
  conn.commit()
  conn.close()
  print("Aizsutits")
  return




def dabut_datus():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute(
    "SELECT Name FROM 'termins'")
  dati = cur.fetchall()
  cur.close()
  conn.close()
  saraksts = []
  for elements in dati:
     saraksts.append(elements[0])
  return saraksts

# izveidot_tabulu()
# ieraksta("pirmais")


# print(dabut_datus())