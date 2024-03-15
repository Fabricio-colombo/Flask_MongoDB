def connect_mongo():
    from config import URI_config, nome_config, collection_name_config
    from pymongo import MongoClient

    URI = URI_config
    nome = nome_config
    collection_name = collection_name_config
    
    try:
        client = MongoClient(URI)
        db = client[nome]
        collection = db[collection_name]
        client.server_info()
        return collection
    except Exception as e:
        print("Connection failed:", e)
        return None
    
if __name__ == "__main__":
    collection = connect_mongo()

    if collection is not None:
        print("Conexão bem-sucedida!")
    else:
        print("Falha ao conectar ao banco de dados.")


