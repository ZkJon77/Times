from models.time_models import time # Importa o modelo time
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os carros
def get_time():
    time = time.query.all()  # Busca todos os times no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de time.',
            'dados': [time.json() for time in time]  # Converte os objetos de carro para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um carro específico por ID
def get_time_by_id(time_id):
    time = time.query.get(time_id)  # Busca o carro pelo ID

    if time:  # Verifica se o carro foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'time encontrado.',
                'dados': time.json()  # Converte os dados do carro para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o carro não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'time não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo carro
def create_time(time_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in time_data for key in ['titulo', 'liga', 'jogadores', 'clube']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, liga, jogadores e clube são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo carro
    novo_time = time(     
        titulo=time_data['titulo'],
        liga=time_data['liga'],
        jogadores=time_data['jogadores'],
        clube=time_data['clube']
    )
    
    db.session.add(novo_time)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'time cadastrado com sucesso.',
            'time': novo_time.json()  # Retorna os dados do time cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

    # Função para atualizar um time por ID
def update_time(time_id, time_data):
    time = time.query.get(time_id)  # Buscar o time pelo ID

    if not time:  # Se o time não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'time não encontrado.'}, ensure_ascii=False),
            404 # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'   #Garante que a resposta seja em json
        return response
    
        # valida se todos os campos obrigatorios foram fornecidos
    if not all(key in time_data for key in ['titulo', 'liga', 'Jogadores', 'clube']):
        response = make_response(
            json.dumps({'mensagem': 'Dados invalidos. titulo, liga, Jogadores e clube são abrigatórios'}, ensure_ascii=False),
            400 # Codigo HTTP 400 para requisição invalida
        )
        response.headers['Content-Type'] = 'application/json'  #define que a resposta é em json
        return response
        
        # Atualiza os dados do carro
    time.titulo = time_data['titulo']
    time.liga = time_data['liga']
    time.jogadores = time_data['jogadores']
    time.clube = time_data['clube']

    db.session.commit()   #confirma a atualização no banco de dados

        # retorna a resposta com os dados do carro atualizado
    response = make_response(
        json.dumps({
            'mensagem': 'time atualizado com sucesso.',
            'time': time.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'   #Define que a resposta é em JSON
    return response