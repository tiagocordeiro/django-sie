# django SIE


### Como rodar o projeto

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/django-sie.git
cd django-sie
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


### Configurar administrador
Para cria um usuário administrador
```
python manage.py createsuperuser --username dev --email dev@foo.bar
```


### Banco de dados para ambiente de desenvolvimento com Docker
```
docker-compose up -d
```


### Rodar em ambiente de desenvolvimento
Para rodar o projeto localmente
```
python manage.py runserver
```
