from flask import Flask, jsonify

app = Flask(__name__)

# Ruta con numero a calcular factorial
@app.route('/factorial/<int:fact>')

def factorial(fact):
    resultado = 1
    for i in range(1, fact + 1):
        resultado *= i

    paridad = "par" if fact % 2 == 0 else "impar"
    return jsonify({
        "numero": fact,
        "paridad": paridad,
        "factorial": resultado
       
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)