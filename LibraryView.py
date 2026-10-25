import mysql.connector

class LibraryManager:
    def __init__(self):
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Achulachu@123",
                database="library_db"
            )
            print("Connection Successful")

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""
                    insert into book(title,author,category,price,published_date)
                    values(%s,%s,%s,%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Book Added Successfully...!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            self.cursor.execute("select*from book")
            records=self.cursor.fetchall()
            for data in records:
                print(data)
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select*from book where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            if record==None:
                print("No Book Found...!")
            print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from book where id=%s"
            value=(id,)
            self.cursor.execute(query,value)
            record=self.cursor.fetchone()
            if record!=None:
                query="delete from book where id=%s"
                self.cursor.execute(query,value)
                self.connection.commit()
                print("Book deleted Successfully...!")
            else:
                print("Book Not Found...!")
        except Exception as e :
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record != None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k+"=%s,"
                    placeholder=placeholder.rstrip(",")
                    query=f"update book set {placeholder} where id=%s"
                    value=[v for v in kwargs.values()]
                    value.append(id)
                    self.cursor.execute(query,value)
                    self.connection.commit()
                    print("Book Updated Successfully")
            else:
                print("Book Not Found")
        except Exception as e:
            print(e)




obj=LibraryManager()

# print(obj.get_object(1))

# obj.post(
#     title="xxx",
#     author="Rodrickxxx",
#     category="Sportsxxx",
#     price=1890,
#     published_date="2020-02-01"
# )

obj.get()
# obj.retrieve(id=4)
# obj.delete(id=5)
# obj.put(id=1,author="Adi")


