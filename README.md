# dsd-socket-t1

  A pasta docs contém os diagramas do projeto
  A arquivo ```src/components/client/demo/run_crud_routine.py``` é uma forma fácil de rodar o cenário de CRUD conectando-se ao servidor:

  Dessa forma:
  ```py src/components/client/demo/run_crud_routine.py```

  Os arquivos de ```config.py``` contém as informações relevantes de endereço de servidor e porta

  Parar rodar os testes unitários/integração

  ```pipenv shell```
  ```pipenv install```
  ```pytest```

  Para rodar o servidor:

  ```py src/components/server/main.py```

  Para rodar o cliente:
  ```py src/components/client/main.py```