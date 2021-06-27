from execute_query import execute_read_one_query, execute_write_query, execute_read_all_query
import fileinput
from flask import Flask, request
from flask_restful import Resource, Api
from format_date import format_date, check_date
from login import get_login_info, create_connection
import sys

app = Flask(__name__)
api = Api(app)
file_path = sys.argv[1:][0]
info = get_login_info(file_path)
connection = create_connection(*info)

def get_students():
    students = []
    query = """select name from students"""
    get_date = execute_read_all_query(connection, query)
    for list in get_date:
        students.append(list[0])
    return students

class Students(Resource):
    def get(self, student_name):
        students = get_students()       
        if student_name not in students:
            return "Name does't exist"
        else:
            query = """select birth_date from students where name='{}'""".format(student_name)
            get_date = execute_read_one_query(connection, query)
            ymd = format_date(get_date)
            birth_date = check_date(ymd, student_name)
            return birth_date
        
    def post(self, student_name):
        birth_date = request.form['date']
        students = get_students()       
        if student_name in students:
            return "Name already exists"
        else:
            query = """insert into students (name, birth_date) values ('{}', '{}')""".format(student_name, birth_date)
            execute_write_query(connection, query)
            return "Successful recording"

api.add_resource(Students, '/<string:student_name>')

if __name__ == '__main__':
    app.run(debug=True)