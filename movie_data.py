import sqlite3

conn = sqlite3.connect('movies_db')

pointer = conn.cursor()

pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")

pointer.execute("INSERT INTO MOVIES VALUES('Doctor','SivaKarthkeyan','PriyankaMohan','SivaKarthikeyan',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Jai Bhim','Surya','Lijomol','GnanaVel',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('Beast','Vijay','Pooja Hegde','Nelson',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Mahaan','Vikram','Simran','Karthik Subburaj',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('Vikram','KamalHasan','Shivani','Lokesh Kanagaraj',2022)")



# Printing all the elements of the database
print("************************Everything in the database************************")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

# In this query, we are printing only the details from the db where Tom Holland is the lead actor
print("************************Actor Query************************")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'Surya'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")