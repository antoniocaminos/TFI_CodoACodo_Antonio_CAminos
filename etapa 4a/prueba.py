# Importamos el framework Flask y la función que nos permit el render de los templates
from flask import Flask, render_template

# Creamos la aplicación
app = Flask(__name__)  #genero instancia del objeto de la clase Flask


# Proporcionamos la ruta a la raiz del sitio
@app.route('/')  #ruteo qu retorna para el archivo html en el raiz
def home():
    return render_template('prueba.html', title='Prueba Flask',
    heading='Bienvenidos a Flask!', items=['Item 1', 'Item 2', 'Item 3'])
    #retornamos la pagina prueba.html con title, heading e items 

# Estas líneas de código las requiere python para que 
# se pueda empezar a trabajar con la aplicación
if __name__ == "__main__":   #hace arrancar la aplicación en modo debug para ver los errores 
    app.run(debug=True)      #Corremos la aplicación en modo debug
    
    #ejecutar desde la terminarl
    #click en 127.0.0.1/5000