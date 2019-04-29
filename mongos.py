from pymongo import MongoClient
import datetime


class MongoHelper(object):
    def __init__(self, url, port, db_name, set_name):
        self.conn = MongoClient(url, port)
        self.db = self.conn[db_name]
        self.my_set = self.db[set_name]

    def insert(self, insert_dict):
        post_id = self.my_set.insert_one(insert_dict).inserted_id
        return post_id

    def update_one(self, filter, post):
        update_result = self.my_set.update_one(filter=filter,
                                               update={'$set': post},
                                               upsert=True)
        return update_result

    def select_one(self, query):
        return self.my_set.find_one(query)

    def select_more(self, query=None, projection=None):
        """ {"time":{"$gt":xxx,"$lte":xxx}},{"_id":0,"time":0} """
        results = self.my_set.find(query, projection=projection)

        return list(results)
    def select_more_df(self,query=None, projection=None):
        import pandas as pd 
        results = self.select_more(query,projection)
        return pd.DataFrame(results)
    def set_count(self, query):
        return self.my_set.find(query).count()

    def insert_many(self,data):
        try:
            self.my_set.insert_many(data)
            return True
        except Exception as e:
            print(e)
            return False

    def __del__(self):
        self.conn.close()



if __name__ == "__main__":
    mongos = MongoHelper("192.168.115.212",27017,"ISP","shaanxi_count")    
    import pprint
    results = mongos.select_more_df({"time":{"$gte":"20180401","$lte":"20180429"}},{"_id":0})
    pprint.pprint(results)

    