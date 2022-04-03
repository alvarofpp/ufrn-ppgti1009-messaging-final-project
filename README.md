# PPGTI1009 - Messaging

Final project of Distributed Programming (PPGTI1009) course of Master's degree in Information Technology
from the Federal University of Rio Grande do Norte (UFRN), with
[Frederico Araujo Da Silva Lopes][ufrn-professor] as professor.

Group:

- Álvaro Ferreira Pires de Paiva
  - Enrolment: 20211028885
  - E-mail: alvarofepipa@gmail.com
- Italo Oliveira Fernandes
  - Enrolment: 20211028965
  - E-mail: italo.oliveira.029@ufrn.edu.br

## How to run

First you need to up the RabbitMQ broker and Postgres database:

```shell
make up-base
```

You can now up the restaurant's front-end and back-end apps:

```shell
make up-restaurant
```

After up the containers, you need to init the restaurant database:

```shell
make restaurant-db-reset
```

You can now test the restaurant API by going to `http://localhost:8000/docs`.

[ufrn-professor]: https://sigaa.ufrn.br/sigaa/public/docente/portal.jsf?siape=2510306
