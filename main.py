from flask import Flask, jsonify
import redis
from waitress import serve

app = Flask(__name__)
cache = redis.Redis()

def calcular_fatorial(numero):
    # Calcula o fatorial de um número inteiro.
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        # Verifica se o resultado está em cache
        cache_key = f"fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado:
            return int(resultado)

        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i

        # Armazena o resultado em cache
        cache.set(cache_key, str(fatorial))
        return fatorial

def calcular_super_fatorial(numero):
    # Calcula o super fatorial de um número inteiro.
    if numero < 0:
        return "Número deve ser não-negativo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        # Verifica se o resultado está em cache
        cache_key = f"super_fatorial:{numero}"
        resultado = cache.get(cache_key)
        if resultado:
            return int(resultado)

        super_fatorial = 1
        for i in range(1, numero + 1):
            super_fatorial *= calcular_fatorial(i)

        # Armazena o resultado em cache
        cache.set(cache_key, str(super_fatorial))
        return super_fatorial
    
# Rota para obter o super fatorial de um número.
@app.route('/super_fatorial/<int:numero>', methods=['GET'])
def obter_super_fatorial(numero):
    # Retorna um JSON contendo o número e o super fatorial calculado.
    resultado = calcular_super_fatorial(numero)
    return jsonify({'numero': numero, 'super_fatorial': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # Executa o aplicativo Flask com o servidor Waitress
    serve(app, host='0.0.0.0', port=6000, url_scheme='https')
