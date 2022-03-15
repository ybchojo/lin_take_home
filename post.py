from flask import Flask, request
import json
import os
import sqlite3

#------------------------------------------------------------ DB ------------------------------------------------------------#
class Model:

    def __init__(self, conn, curr):
        self.conn = conn
        self.curr = curr
        self.word = []
        self.col = [('word', 'VARCHAR (255)', 'PRIMARY KEY')]
    def create_table(self, table_name):
        try:
            query = 'create table if not exists ' + '%s(' % table_name
            for i in range(len(self.col)):
                sql = ''
                for c in self.col[i]:
                    sql += c + ' '
                if i == len(self.col) -1:
                    query += sql
                else:
                    query += sql + ','
            self.curr.execute(query + ');')
            # commit changes in the database
            self.conn.commit()
        except:
            print("Oops! There is an error")

    def select(self, column, table):
        try:
            query = 'SELECT %s FROM %s' % (column, table)
            self.curr.execute(query)
            self.word = []

            for c in self.curr.fetchall():# Fetching 1st row from the table
                self.word.append(c[0])
            return self.word
        except:

            print("Oops! There is an error - SELECT")

    def insert(self, word ,table):
        try:

            for value in word:
                if value not in self.word:
                    query = 'insert into %s VALUES (\'%s\');' % (table, value)
                    self.curr.execute(query)
                    self.conn.commit()
            return True

        except:
            print("Oops! There is an error - INSERT")


#------------------------------------------------------------ microservice ------------------------------------------------------------#

base_words = {
	"vocab": [
			"#ad",
			"#sponsored",
			"advertisement"
	]
}

app = Flask(__name__)

conn = sqlite3.connect(':memory:', check_same_thread=False, timeout=1000) # CONNECT THE SQLITE3
cursor = conn.cursor()
# print('Cursor Type : ', type(cursor))
col = [('word', 'VARCHAR (255)', 'PRIMARY KEY')]
db = Model(conn, cursor)
# create table
db.create_table('vocab')
db.insert(list(base_words.values())[0], 'vocab') #insert initial words


@app.route("/api/vocab",methods=['GET'])
def get():
    vocab_words = db.select(col[0][0], 'vocab')
    return {'vocab': vocab_words}

@app.route('/api/vocab', methods = ['POST'])
def post():
    request_data = request.get_json()
    add_words = request_data['vocab']

    insert_words = db.insert(add_words, 'vocab')
    new_words = db.select(col[0][0], 'vocab')

    return {'vocab': new_words}

@app.route("/api/prediction", methods=['POST'])
def predict():

    words = request.get_json()
    output = {"prediction": "non-sponsored"}
    post_txt = words['post_text'].split()
    current_words = db.select(col[0][0], 'vocab')

    for x in post_txt:
        if x in current_words:
            output['prediction'] = "sponsored"
        else:
            return output

if __name__ == '__main__':
    app.run(debug=False, port=2000)