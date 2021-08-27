import json
import os
import pymysql

class Dao:


    def __init__(self, config='mysqlConfig.json'):
        self.__connection = None
        self.__cursor = None
        with open(os.path.dirname(__file__) + os.sep + config, 'r', encoding='utf-8') as f:
            self.__config = json.load(f)

    def getConnection(self):
        if self.__connection:
            return self.__connection

        try:
            self.__connection = pymysql.Connect(**self.__config)
            return self.__connection
        except Exception as e:
            print("Exception" + str(e))

    def getCursor(self):
        if self.__cursor:
            return self.__cursor

        try:
            self.__cursor = self.getConnection().cursor()
            return self.__cursor
        except Exception as e:
            print("Exception" + str(e))

    def execute(self, sql, params=None):
        if params:
            try:
                self.__cursor = self.getCursor()
                resul = self.getCursor()
                result = resul.execute(sql, params)
                return result
            except Exception as e:
                print(str(e))
                self.rollback()
        else:
            try:
                result = self.getCursor().execute(sql)
                return result
            except Exception as e:
                print(e)
                self.rollback()

    def rollback(self):
        return self.getConnection().rollback()

    def commit(self):
        self.getConnection().commit()

    def fetchall(self):
        self.getCursor().fetchall()

    def fetchone(self):
        self.getCursor().fetchone()

    def close(self):
        if self.__cursor:
            self.__cursor.close()
        if self.__connection:
            self.__connection.close()


if __name__ == '__main__':
    dao = Dao()
    sql = "insert into csdndata values (%s,%s,%s,%s)"
    dao.execute(sql, ['100', 'https://baidu.com', '标题', '内容'])
    dao.commit()
    dao.close()
