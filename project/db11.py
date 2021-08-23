import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="runoob_db" # when you linked mysql, you choose create a database, here is the database name
)
mycursor = mydb.cursor()

class Mysql():
  def __init__(self, data):
      self.data = data
  
  # insert method
  def insert(data):
    country = str(data['country']['name'])
    name = str(data['name'])
    list1 = data['type']
    holidays_type =''.join(list1)
    holidays_date = str(data['date']['iso'])
    description = str(data['description'])

    sql = "insert into holidays (country, name, type, iso_date, description) values (%s, %s, %s, %s, %s)"
    val = (country, name, holidays_type, holidays_date, description)
    mycursor.execute(sql, val)
    mydb.commit()
    output ={"status" : "insert success"}
    return output

  # select method
  def select1():
    mycursor.execute("SELECT * FROM holidays")
    myresult = mycursor.fetchall()     # fetchall() selcet all data
    for x in myresult:     
      return x

  # update method
  def update1(old,new):
    sql = "UPDATE holidays SET name = %s WHERE name = %s"
    val = (new, old)
    mycursor.execute(sql, val)
    mydb.commit()
    count = int(mycursor.rowcount)
    if count==0:
      ss ={"status" : "no update "}
      return ss
    else:
      output ={"status" : "update success"}
      return output
  
  # delete method
  def delete1(data):
    sql = "DELETE FROM holidays WHERE name = %s"
    val = (data, )
    mycursor.execute(sql, val)
    mydb.commit()
    count = int(mycursor.rowcount)
    if count==0:
      ss ={"status" : "no data to delete"}
      return ss
    else:
      output ={"status" : "delete success"}
      return output
