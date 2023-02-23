import pymongo

#Membuat koneksi url mongo

koneksi_url = "mongodb://localhost:27017"

def cekKoneksi() :
    client =  pymongo.MongoClient(koneksi_url)
    try:
        cek = client.list_database_names()
        print(cek)
    except:
        print('database error')
# cekKoneksi()


def createDatabase():
    myclient = pymongo.MongoClient(koneksi_url)
    mydatabase = myclient['dbTB']
    mycollection = mydatabase['material']
    mydocument = mycollection.insert_one({ 'kode': 'BTK001', 'nama_material' : 'batu bata', 'harga' : '1000', 'stok': '250000' })

    return mydocument
# createDatabase()

class MongoCRUD:
    def __init__(self,data,koneksi):
        self.client = pymongo.MongoClient(koneksi)
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    
    def read(self):
        documents = self.collection.find()
        value = [{
            item: data[item] for item in data if item != '_id'} for data in documents]
        return value

if __name__ == '__main__':
    data = {
        # nama database yang akan disambungkan
        "database": "dbTB",
        # nama collection yang akan di sambungkan
        "collection": "material",
    }

    mongo_objek = MongoCRUD(data, koneksi_url)
    read_data =  mongo_objek.read()
    print(read_data)