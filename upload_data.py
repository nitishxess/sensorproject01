from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://nitishxess2:VtQZAkRVLAiH7qlW@cluster0.mracr.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="BHALOA"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\Asus\OneDrive\Desktop\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)