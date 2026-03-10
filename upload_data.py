from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url="mongodb+srv://harsh:95089harsh@cluster0.ekc56bn.mongodb.net/?appName=Cluster0"

#client
client= MongoClient(url) 


#Database name and collection name
DATABASE_NAME="harsh"
COLLECTION_NAME="waferfault"

df=pd.read_csv("E:\sensorproject\notebooks\wafer_23012020_041211.csv")

df.head()

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)