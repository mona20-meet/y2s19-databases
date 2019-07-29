from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	__tablename__= "paintings"
	Name= Column(String, primary_key=True)
	artist=Column(String)
	year=Column(Integer)
	value=Column(Integer)
	def __repr__(self):
		return ("Name: {}\n"
				"Artist Name: {} \n"
				"Year of Orgin: {} \n"
				"Value: {}").format(
					self.Name, self.artist, self.year, self.value)

table1= Knowledge	(Name= 'Mona Lisa', artist= 'Leonardo da Vinci', year=1503, value=650000000)
print(table1)