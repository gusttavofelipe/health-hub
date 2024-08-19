## Stack

A Aplicação foi desenvolvida utilizando o `Django`. Para salvar os dados está sendo utilizado o `postgres`, por meio do `docker`.

## Execução
Primeiro você precisa do `pyenv`, para gerenciar o `python` e o ambiente virtual.

Em seguida crie e ative seu ambiente virtual usando pyenv, executando respectivamente:
```bash
pyenv virtualenv 3.12.4 health-hub
pyenv activate health-hub
```

Instale as dependencias executando:
```bash
pip install -r requirements.txt
```

### Variável de ambiente Django
Em seguida execute o comando `python` para ter acesso ao shell interativo.

No shell, digite o seguinte comando para importar a função que irá gerar sua SECRET_KEY:
```bash
from django.core.management.utils import get_random_secret_key
```

Ainda no shell interativo, execute o comando abaixo para gerar e exibir sua SECRET_KEY:
```bash
print(get_random_secret_key())
```

Copie o valor gerado e atribua a variavel `SECRET_KEY` em seu arquivo `.env`

### Banco de dados

Para subir o banco de dados, caso não tenha o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
docker-compose up -d
```

### Migrações

Para aplicar as migrações, execute:
```bash
task migrate
```

### Executar aplicação

Para subir a aplição, execute:
```bash
task run
```

Em seguida, para visualizar abra seu navegador no endereço: http://127.0.0.1:8000/
