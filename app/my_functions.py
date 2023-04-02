import string
import random 
import json
import datetime

def get_random_string(length):
    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    return(result_str)

def populate_database(database,database_model,json_file):
    with open(json_file) as file:
        json_file = json.loads(file.read())
    for line in json_file:
        user = database_model(id         = line['id'],
                              name       = line['name'],
                              gender     =  line['gender'],
                              breed      = line['breed'],
                              birth_date = datetime.datetime.strptime(line['date'],"%Y%m%d").date(),
                              details    = line['details'],
                              price      = line['price'],
                              image      = line['image'])
        database.session.add(user)
    database.session.commit()    

