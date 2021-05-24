from api.hello_api import HelloWorld
# from api.categoria_api import CategoriaAPI
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
mysql = MySQL(app) #toma nuestro obje e inicializa / amplia nuestra funcuionalidad de nuestra app
api = Api(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootcodigo8'
app.config['MYSQL_DB'] = 'myblog'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

class PostCategoriaAPI(Resource):
  def get(self, id):   
    cur = mysql.connection.cursor()
    cur.execute('''select p.titulo, c.nombre as categoria from myblog.post as p left join myblog.categoria as c on p.idcategoria = c.idcategoria where p.idcategoria= ''' + id )
    result = cur.fetchall()
    return str(result)

class CategoriaAPI(Resource):
  def get(self):   
    cur = mysql.connection.cursor()
    cur.execute("select * from categoria")
    result = cur.fetchall()
    return str(result)

class PostAPI(Resource):
  def get(self):   
    cur = mysql.connection.cursor()
    cur.execute("select * from post")
    result = cur.fetchall()
    return str(result)

api.add_resource(PostAPI, '/post')#agregar recurso
api.add_resource(CategoriaAPI, '/categoria')
api.add_resource(PostCategoriaAPI, '/categoria/<id>/post')