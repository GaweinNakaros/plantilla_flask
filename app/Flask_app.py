
# Flask App Template
# Este es el módulo principal de Flask que importa las funciones necesarias para crear la aplicación, renderizar plantillas HTML, manejar solicitudes y responder con JSON.

from flask import Flask, render_template, request, jsonify  

# Create Flask app
app = Flask(__name__)  # Crea una instancia de la aplicación Flask. '__name__' indica el módulo actual, lo cual ayuda a Flask a encontrar recursos.

# Configuration settings
#app.config['SECRET_KEY'] = 'your_secret_key_here'  # Establece una clave secreta utilizada para la seguridad de la aplicación, como firmar cookies o manejar sesiones.
app.config['DEBUG'] = True  # Activa el modo de depuración para desarrollo. Cambiar a False en producción.

# Routes
@app.route('/')  # Define una ruta para la URL base ('/') y asigna la función 'home' para manejar solicitudes a esta ruta.
def home():
    return render_template('index.html')  # Maneja solicitudes a la ruta base ('/'). Devuelve la plantilla HTML 'index.html'.

@app.route('/api/data', methods=['GET', 'POST'])  # Define una ruta '/api/data' que acepta solicitudes GET y POST.
def api_data():
    if request.method == 'GET':
        return jsonify({"message": "GET request received!"})  # Comprueba si la solicitud es de tipo GET y responde con un mensaje en JSON.
    elif request.method == 'POST':
        data = request.json  # Obtiene datos en formato JSON del cuerpo de la solicitud POST.
        return jsonify({"received": data})

# Error handling
@app.errorhandler(404)  # Define un controlador personalizado para errores 404 (página no encontrada).
def not_found_error(error):
    return render_template('404.html'), 404  # Renderiza una página HTML personalizada cuando ocurre un error 404.

@app.errorhandler(500)  # Define un controlador personalizado para errores 500 (error interno del servidor).
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500  # Devuelve una respuesta en JSON con un mensaje de error 500.

# Run the app
if __name__ == '__main__':  # Comprueba si el archivo se ejecuta directamente y no como módulo importado.
    app.run(host='0.0.0.0', port=5000)  # Inicia el servidor Flask en todas las interfaces de red ('0.0.0.0') en el puerto 5000.

