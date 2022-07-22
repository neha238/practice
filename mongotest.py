import pymongo


client = pymongo.MongoClient("mongodb+srv://neharani123:Neharani123@neha.ajsmjl2.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"neha",
    "email" : "neha@gmail.com",
    "surname" : "rani"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
