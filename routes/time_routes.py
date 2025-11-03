from flask import Blueprint, request  
from controllers.time_controllers import get_time, create_time, get_time_by_id, update_time

# Define um Blueprint para as rotas de "Carro"
time_routes = Blueprint('time_routes', __name__)  

# Rota para listar todos os carros (GET)
@time_routes.route('/time', methods=['GET'])
def time_get():
    return get_time()

# Rota para buscar um carro pelo ID (GET)
@time_routes.route('/time/<int:time_id>', methods=['GET'])
def time_get_by_id(time_id):
    return get_time_by_id(time_id)

# Rota para criar um novo carro (POST)
@time_routes.route('/time', methods=['POST'])
def time_post():
    return create_time(request.json)

@time_routes.route('/time/<int:time_id>', methods=['put'])
def time_put(time_id):
    time_data = request.json
    return update_time(time_id, time_data)

