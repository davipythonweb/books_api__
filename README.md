# books_api__

* Api com Django-Rest-Framework para e-books 

<summary>e-books_api</summary>


<details>

`ìnicial`

- CRUD de e-books
`django_restframework`
`permissoes admin -> all`
`permissoes user -> safe_methods= GET, HEAD, OPTIONS`


- Autenticação
`djangorestframework-simplejwt`

- comandos Django/bash
`django-admin startproject core .`
`python manage.py migrate`
`python manage.py createsuperuser`
`python manage.py runserver`
`python manage.py startapp <nome_do_app>`
`python mange.py makemigrations`

- adm controller
`admsuper`
`Adm$50001`

- user_teste
`user-test`
`book@reading`

</details>

## pytest

`pip install pytest pytest-django`
`pip install pytest-watch`

### usage

- executar scripts powershell

`set-executionpolicy unrestricted`

-runing pytest- rodar no terminal => pytest

- para ver tudo => pytest -rP

- runing unitest- para o test_django => python manage.py test
- com lib pytest-watch => ptw

#### Database
`postgresql`

##### lib para conexao
`pip install psycopg2`

- acessar o postgres pelo powershell
`psql -U postgres`

- ver versao do postgres pelo powershell
`psql --version`

- listar todas as tabelas do postgres
`\l`

- criar database no shell com comando SQL
`CREATE DATABASE bookstore;`


- urls para abreviações de paises
`https://www.pucsp.br/~acomin/recursos/codpais.html`