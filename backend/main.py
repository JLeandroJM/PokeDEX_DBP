#Flask
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/calcular_tamano', methods=['POST'])
def calcular_tamano():
    start_time = time.perf_counter()  # Capturar el tiempo de inicio de la solicitud
    data = request.get_json()  # Obtener datos JSON del cuerpo del request
    query = data.get('query', '')  # Obtener el valor de la clave 'query' del JSON

    # Calcular el tamaño de la cadena de consulta
    tamano_query = len(query)
    
    
    end_time = time.perf_counter()  # Capturar el tiempo de finalización de la solicitud
    tiempo_respuesta = end_time - start_time  # Calcular el tiempo de respuesta en segundos

    # Crear un JSON de respuesta con el tamaño de la cadena de consulta y el tiempo de respuesta
    response = {
        'tamano_query': tamano_query,
        'tiempo_respuesta': tiempo_respuesta
    }

    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True)
