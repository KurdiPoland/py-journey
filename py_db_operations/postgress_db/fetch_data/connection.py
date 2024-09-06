import psycopg2
import os
import sys

configuration = {
        'db_host' : os.environ.get("DB_HOST").strip(),
        'db_name' : os.environ.get("DB_NAME").strip(),
        'db_user_name' : os.environ.get("DB_USER_NAME").strip(),
        'db_pwd' : os.environ.get("DB_PWD").strip(),
        'db_port' : os.environ.get("DB_PORT").strip()
}

print(configuration)

class Config:

    def __init__(self):
        self._config_ = configuration

    def get_properties( self, config_name: str) -> str:
        if config_name not in self._config_.keys():
            return None
        return self._config_[config_name]
def main():
    config = Config()

    connection = psycopg2.connect(
                                  database=config.get_properties("db_name"),  
                                  user=config.get_properties("db_user_name"), 
                                  password=config.get_properties("db_pwd"), 
                                  host=config.get_properties("db_host"), 
                                  port=config.get_properties("db_port")
                                )
    cursor  = connection.cursor()
    cursor.execute("select table_name from information_schema.tables where table_schema = 'public';")

    #Fetch a single row using fetchone() method
    data = cursor.fetchall()
    connection.close()

    print("Data:", data)
    for rekord in data:
        print(type(rekord))

if __name__ == "__main__" :
    main()
