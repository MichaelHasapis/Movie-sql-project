import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import psycopg2

# Update connection string information

#[!INCLUDE [applies-to-postgresql-single-server](../includes/applies-to-postgresql-single-server.md)]


host = "csstudentsgroupdb2021.postgres.database.azure.com"
dbname = "postgres"
user = "examiner@csstudentsgroupdb2021"
password = "Data_Base_Projects_2022"
sslmode = "require"

# Construct connection string

#[!INCLUDE [applies-to-postgresql-single-server](../includes/applies-to-postgresql-single-server.md)]


conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

#exercise 1


##cursor.execute("Select COUNT(id),extract(year from  release_date) as year from movie GROUP by year order by year;")
##exercise1 = cursor.fetchall()
##setd = []
##setm = []
##for item in exercise1:
##    if(item[1] != None):
##        setd.append(int(item[1]))
##for item in exercise1:
##    if(item[1] !=None):
##        setm.append(item[0])
##
##
##plt.bar(setd,setm,label = "amount of movies")
##plt.legend()
##plt.xlabel('Year')
##plt.ylabel('Number of Movies')
##plt.title('exercise 1')
##plt.show()


##exercise 2
##cursor.execute("select g.id, g.name, count(m.movie_id) as counter from genre g full outer join movie_genres m on m.genre_id = g.id group by g.id, g.name")
##exercise2 = cursor.fetchall()
##setg = []
##setm = []
##for item in exercise2:
##    if(item[1] != None):
##        setg.append(item[1])
##for item in exercise2:
##    if(item[1] !=None):
##        setm.append(item[2])
##print(setg)
##print(setm)
##
##plt.barh(setg,setm,label = "amount of movies",color = "pink")
##plt.legend()
##plt.xlabel('Genre')
##plt.ylabel('Number of Movies')
##plt.title('exercise 2')
##plt.show()

#exercise 4

##cursor.execute("SELECT max(budget), extract(year from  release_date) as year from movie GROUP by year ORDER by year;")
##exercise4 = cursor.fetchall()
##setd = []
##setm = []
##for item in exercise4:
##    if(item[1] != None):
##        setd.append(int(item[1]))
##for item in exercise4:
##    if(item[1] !=None):
##        setm.append(item[0])


##plt.bar(setd,setm,label = "Budget", color= 'c')
##plt.legend()
##plt.xlabel('Year')
##plt.ylabel('Biggest budget')
##plt.title('exercise 4')
##plt.show()

#exercise 5

##cursor.execute("select a.name,sum(m.revenue) as counter_rev,count(m.id) as counter_mov, extract(year from m.release_date) as year from actor a full outer join movie_cast mc on mc.person_id = a.person_id full outer join movie m on m.id = mc.movie_id where a.name = 'Robert De Niro' group by a.name,year order by year;")
##exercise5 = cursor.fetchall()
##setd = []
##setr = []
##for item in exercise5:
##    if(item[1] != None):
##        setd.append(item[3])
##for item in exercise5:
##    if(item[1] !=None):
##        setr.append(item[1])


##plt.bar(setd,setr,label = "Robert De Niro", color= 'g')
##plt.legend()
##plt.xlabel('Year')
##plt.ylabel('Biggest budget')
##plt.title('exercise 5')
##plt.show()

#exercise 6

##cursor.execute("select avg(rating), user_id from ratings group by user_id;")
##exercise6 = cursor.fetchall()
##setu = []
##setr = []
##for item in exercise6:
##    if(item[1] != None):
##        setu.append(item[1])
##for item in exercise6:
##    if(item[1] !=None):
##       setr.append(item[0])


##plt.scatter(setu,setr,s=25,label = "Average rating", color= '#dd1968', edgecolor='black')
##plt.legend()
##plt.xlabel('User')
##plt.ylabel('Average Rating')
##plt.title('exercise 6')
##plt.show()

#exercise 7

cursor.execute("select count(rating), user_id from ratings group by user_id;")
exercise7 = cursor.fetchall()
setu = []
setr = []
for item in exercise7:
    if(item[1] != None):
        setu.append(item[1])
for item in exercise7:
    if(item[1] !=None):
       setr.append(item[0])


plt.scatter(setu,setr,s=25,label = "Rating Amount", color= '#AF38EB', edgecolor='black')
plt.legend()
plt.xlabel('User')
plt.ylabel('Amount of ratings')
plt.title('exercise 7')
plt.show()

#exercise 8

cursor.execute("SELECT r.user_id,avg(r.rating),count(r.user_id) from ratings r group by user_id;")
exercise8 = cursor.fetchall()
seta = []
setr = []
for item in exercise8:
    if(item[0] != None):
        seta.append(item[2])
for item in exercise8:
    if(item[0] !=None):
       setr.append(item[1])


plt.scatter(seta,setr,s=25,label = "User", color= '#fc0303', edgecolor='black')
plt.legend()
plt.xlabel('Amount of ratings')
plt.ylabel('Average rating')
plt.title('exercise 8')
plt.show()


# Clean up

conn.commit()
cursor.close()
conn.close()
