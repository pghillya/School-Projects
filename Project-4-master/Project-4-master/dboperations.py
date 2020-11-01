#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pip._internal import main
main(['install','mysql-connector-python-rf'])


# In[30]:
try:

	import mysql.connector as mysql
	db = mysql.connect(host="HillyardDesktop.HillyardHouse", user="testuser",passwd="P@ssword1", auth_plugin="mysql_native_password")
	cursor = db.cursor()
	cursor.execute("INSERT INTO Project_4.Faculty(firstname, lastname, coursename, courselocation) VALUES('Johnny', 'Smith','Intro to Centos7','Hillsborough st');")
	cursor.execute("SELECT * FROM Project_4.Faculty;")
	data = cursor.fetchall()
	writetofile = print(data)
	f = open('output.txt','a+')
	f.write(str(data))
	cursor.close()
	db.close()
except:
	print("You have caused an error. Please try again.")

# In[ ]:





# In[ ]:




