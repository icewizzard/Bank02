import sqlalchemy as db
import psycopg2

engine = db.create_engine('postgresql+psycopg2://yoni:yoni123@localhost:5432/bank')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('users', metadata, autoload=True, autoload_with=engine)

print(repr(metadata.tables['users']))
#להסתכל באינרנט מה ששמרתי

#https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91 sqlalchemy
#https://www.w3schools.com/python/pandas/default.asp pandas toutrial