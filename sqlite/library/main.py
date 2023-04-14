from visitor import Visitor
import sqlite3

vis = Visitor(
    id=1,
    name="Ahmet",
    surname="Demir",
    age=18,
    email="ahmetyusufdmr88@gmail.com"
)

vis2 = Visitor(
    id=2,
    name="Can",
    surname="Kankilic",
    age=19,
    email="cankankilic@gmail.com"
)

conn = sqlite3.connect('library/library.db')
c = conn.cursor()

# c.execute("""CREATE TABLE visitors (
#     id integer,
#     name text,
#     surname text,
#     age integer,
#     email text
#     )""")   

def insert_visitor(visitor):
    with conn:
        c.execute("INSERT INTO visitors VALUES (:id, :name, :surname, :age, :email)", 
                {'id': visitor.id, 'name': visitor.name, 'surname': visitor.surname,
                    'age': visitor.age, 'email': visitor.email})
        
def get_by_id(id):
    c.execute("SELECT * FROM visitors WHERE id=:id", {'id': id})
    return c.fetchone()

def remove_vis(id):
    with conn:
        c.execute("DELETE from visitors WHERE id = :id",
                  {'id': id})


conn.commit()
conn.close()
