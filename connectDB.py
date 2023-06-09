import mysql.connector

class gestLocation:
  def __init__(self):
    try:
      self.cnt = mysql.connector.connect(host="localhost", user="root", password="123456")
      self.cntCursor = self.cnt.cursor()
      self.queries = ['CREATE DATABASE IF NOT EXISTS admintables', 'USE admintables',
                 'create table if not exists Location(id int primary key,ref char(10) not null,idClient int,matricule char(50),date_emprunt date not null,date_retour date not null,foreign key (idClient) references Clients(id),FOREIGN KEY (matricule) REFERENCES voitures(matricule))']
      for q in self.queries:
        self.cntCursor.execute(q)
    except:
      pass
    try:
      self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="admintables"
      )
      self.mycursor = self.mydb.cursor()
    except:
      pass
  def selectRef(self,str1):
    self.mycursor.execute(f"SELECT * from Location WHERE ref = %s",(str1,))
    return self.mycursor.fetchall()
  def selectALL(self):
    self.mycursor.execute("SELECT * FROM Location")
    return self.mycursor.fetchall()
  def selectId(self,id1):
    self.mycursor.execute(f"SELECT * FROM Location WHERE id = {id1}")
    return self.mycursor.fetchone()
  def deleteId(self,id1):
    self.mycursor.execute(f"DELETE FROM Location WHERE id = {id1}")
    self.mydb.commit()
  def insertTbl(self,tpl):
    self.mycursor.execute('INSERT INTO Location(id,ref,idClient,matricule,date_emprunt,date_retour) VALUES (%s,%s,%s,%s,%s,%s)', tpl)
    self.mydb.commit()
  def updateTbl(self,tpl):
    self.mycursor.execute('UPDATE Location SET ref = %s,idClient = %s,matricule = %s,date_emprunt = %s,date_retour = %s WHERE id = %s',tpl)
    self.mydb.commit()
class gestClients:
  def __init__(self):
    try:
      self.cnt = mysql.connector.connect(host="localhost", user="root", password="123456")
      self.cntCursor = self.cnt.cursor()
      self.queries = ['CREATE DATABASE IF NOT EXISTS admintables', 'USE admintables',
                 'create table if not exists Clients(id int primary key,nom char(50) not null,prenom char(50) not null,age int not null,email char(50) not null,tele char(20) not null,adresse char(100) not null,id_empl int,foreign key id_empl references employee(id))']
      for q in self.queries:
        self.cntCursor.execute(q)
    except:
      pass
    try:
      self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="admintables"
      )
      self.mycursor = self.mydb.cursor()
    except:
      pass
  def selectNom(self,str1):
    self.mycursor.execute(f"SELECT * from Clients WHERE nom = %s",(str1,))
    return self.mycursor.fetchall()
  def selectALL(self):
    self.mycursor.execute("SELECT * FROM Clients")
    return self.mycursor.fetchall()
  def selectId(self,id1):
    self.mycursor.execute(f"SELECT * FROM Clients WHERE id = {id1}")
    return self.mycursor.fetchone()
  def deleteId(self,id1):
    self.mycursor.execute(f"DELETE FROM Clients WHERE id = {id1}")
    self.mydb.commit()
  def insertTbl(self,tpl):

      self.mycursor.execute('INSERT INTO Clients(id,nom,prenom,age,email,tele,adresse,id_empl) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', tpl)
      self.mydb.commit()

  def updateTbl(self,tpl):
    self.mycursor.execute('UPDATE Clients SET nom = %s,prenom = %s,age = %s,email = %s,tele = %s,adresse = %s WHERE id = %s',tpl)
    self.mydb.commit()


class gestVoiture:
  def __init__(self):
    try:
      self.cnt = mysql.connector.connect(host="localhost", user="root", password="123456")
      self.cntCursor = self.cnt.cursor()
      self.queries = ['CREATE DATABASE IF NOT EXISTS admintables', 'USE admintables',
                 'create table if not exists voitures(id int primary key,matricule char(50) not null,Marque char(50) not null,Annee char(5) not null,Modele char(50) not null,Carburant char(20) not null,PrixJour char(100) not null)']
      for q in self.queries:
        self.cntCursor.execute(q)
    except:
      pass
    try:
      self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="admintables"
      )
      self.mycursor = self.mydb.cursor()
    except:
      pass
  def selectByMatricule(self,str1):
    self.mycursor.execute("SELECT * from voitures WHERE matricule = %s", (str1,))
    return self.mycursor.fetchone()
  def selectMatr(self,tpl):
    self.mycursor.execute("SELECT matricule from voitures WHERE Marque = %s and Modele = %s and Annee = %s",(tpl[0],tpl[1],tpl[2],))
    return self.mycursor.fetchone()
  def selectMarque(self,str1):
    self.mycursor.execute("SELECT * from voitures WHERE Marque = %s",(str1,))
    return self.mycursor.fetchall()

  def selectALL(self):
    self.mycursor.execute("SELECT * FROM voitures")
    return self.mycursor.fetchall()
  def selectId(self,id1):
    self.mycursor.execute(f"SELECT * FROM voitures WHERE id = {id1}")
    return self.mycursor.fetchone()
  def deleteId(self,id1):
    self.mycursor.execute(f"DELETE FROM voitures WHERE id = {id1}")
    self.mydb.commit()
  def insertTbl(self,tpl):
    self.mycursor.execute('INSERT INTO VOITURES(id,matricule,Marque,Annee,Modele,Carburant,PrixJour) VALUES (%s,%s,%s,%s,%s,%s,%s)', tpl)
    self.mydb.commit()
  def updateTbl(self,tpl):
    self.mycursor.execute('UPDATE voitures SET matricule = %s,Marque = %s,Annee = %s,Modele = %s,Carburant = %s,PrixJour = %s WHERE id = %s',tpl)
    self.mydb.commit()


class gestionEmployee:
  def __init__(self):
    try:
      self.cnt = mysql.connector.connect(host="localhost", user="root", password="123456")
      self.cntCursor = self.cnt.cursor()
      self.queries = ['CREATE DATABASE IF NOT EXISTS admintables', 'USE admintables',
                 'create table if not exists employee(id int primary key,nom char(100) not null,prenom char(50) not null,poste char(5) not null,tele char(14) not null,username char(20) not null,password char(100) not null)']
      for q in self.queries:
        self.cntCursor.execute(q)
    except:
      pass
    try:
      self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="admintables"
      )
      self.mycursor = self.mydb.cursor()
    except:
      pass
  def selectUsername(self,str1):
    self.mycursor.execute(f"SELECT * from employee WHERE username = %s",(str1,))
    return self.mycursor.fetchall()
  def selectALL(self):
    self.mycursor.execute("SELECT * FROM employee")
    return self.mycursor.fetchall()
  def selectId(self,id1):
    self.mycursor.execute(f"SELECT * FROM employee WHERE id = {id1}")
    return self.mycursor.fetchone()
  def deleteId(self,id1):
    self.mycursor.execute(f"DELETE FROM employee WHERE id = {id1}")
    self.mydb.commit()
  def insertTbl(self,tpl):
    self.mycursor.execute('INSERT INTO employee(id,nom,prenom,poste,tele,username,password) VALUES (%s,%s,%s,%s,%s,%s,%s)', tpl)
    self.mydb.commit()
  def updateTbl(self,tpl):
    self.mycursor.execute('UPDATE employee SET nom = %s,prenom = %s,poste = %s,tele = %s,username = %s,password = %s WHERE id = %s',tpl)
    self.mydb.commit()


