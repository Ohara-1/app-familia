import os
import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao PYTHONPATH
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

# Agora podemos importar do pacote backend
from backend import create_app, db

app = create_app()

def get_env():
    return os.environ.get('FLASK_ENV', 'production')

def get_debug(env):
    return env == 'development'

# Configuração para ambiente de produção
app.config['ENV'] = get_env()
app.config['DEBUG'] = get_debug(get_env())

# Criar tabelas do banco de dados
with app.app_context():
    db.create_all()

# Para desenvolvimento local
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

# Para o Vercel
app = app 