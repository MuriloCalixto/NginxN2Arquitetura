# DOCUMENTAÇÃO DA API DE CALCULO DO SUPER FATORIAL.

Essa API tem a função principal de criar o super fatorial de um número inteiro, que é o produto de todos os fatoriais de 1 até o número fornecido.
O Redis é usado como um cache para armazenar os resultados dos cálculos. A biblioteca Waitress é usada para servir a aplicação Flask em um servidor.
O endpoint /super_fatorial/<int:numero> é definido para receber um número como parâmetro na URL e retorna o número e seu super fatorial em formato JSON.

**(OBS: Certifique-se de ter as bibliotecas Flask, Redis e Waitress instaladas para executar a API corretamente.)**
