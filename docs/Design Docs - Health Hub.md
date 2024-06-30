# Health Hub

## Resumo
Este documento traz informações do desenvolvimento de um serviço (website)
capaz de armazenar registros de informações de saúde de uma comunidade.

## Objetivo
Essa aplicação tem como objetivo principal ajudar profissionais de saúde a gerenciar os dados de seus pacientes de maneira mais simplificada e eficiente.

## O que é?
Uma aplicação que:
- armazena e disponibiliza informações.

## O que não é?
Uma aplicação que:
- se comunica com serviços externos.

## Solução Proposta
Desenvolvimento de uma aplicação web com interface intuitiva e amigável, projetada para armazenar de forma segura e acessível as informações de saúde dos pacientes, de modo que o profissional responsável seja capaz de fazer análises prévias que o ajudarão no atendimento antes mesmo do encontro com o paciente. O site disponibilizará sistemas de login para que cada profissional tenha sua área própria restrita e de gerenciamento.

### Arquitetura
![Desenho da arquitetura](images/architecture.png)

## Diagramas de sequência

#### Diagrama de listagem de registros
```mermaid
sequenceDiagram
    title List Personal Health Records
    participant Client
    participant View
    participant Database

    Client->>+View: GET /records
    View->>+Database: Query all records
    Database-->>View: Return list of records
    View-->>Client: Return records data
    Note right of Client: Status Code: 200 - Ok
```

#### Diagrama de detalhe de um registro

```mermaid
sequenceDiagram
    title Get Personal Health Record
    participant Cliente
    participant View
    participant Database

    Cliente->>+View: GET /records/{number}
    Note right of Cliente: Path Params:<br/>- register_id: <register_id>
    View->>+Database: Query record by id
    alt Record found
        Database-->>View: Return record
        View-->>Cliente: Return record
        Note right of Cliente: Status Code: 200 - Ok
    else Record not found
        Database-->>View: Return null
        View->>-Cliente: Return Error Response
        Note right of Cliente: Status Code: 404 - Not Found
    end
    opt Internal Server Error
        Database--x View: Throws error
        View-x Cliente: Return Error Response
        Note right of Cliente: Status Code: 500 - Internal Server Error
    end
```

#### Diagrama de postagem de um registro

```mermaid
sequenceDiagram
    title Create Personal Health Record
    participant Cliente
    participant View
    participant Database

    Cliente->>+View: POST /records
    Note right of Cliente: Request Body:<br/>- record_data: {PersonalHealthRecord}
    View->>+Database: Create new record
    alt Record created successfully
        Database-->>View: Return newly created record
        View-->>Cliente: Return successful response
        Note right of Cliente: Status Code: 201 - Created
    else Internal Server Error
        Database--x View: Throws error
        View-x Cliente: Return Error Response
        Note right of Cliente: Status Code: 500 - Internal Server Error
    end
```

#### Diagrama de atualização de um registro
```mermaid
sequenceDiagram
    title Update Health Record
    participant Client
    participant View
    participant Database

    Client->>+View: PUT /records/{record_id}
    Note right of Client: Path Params:<br/>- record_id: <record_id>
    Client->>+View: Request Body:<br/>- record_data: {...}
    View->>+Database: Query record by id
    Database-->>View: Return existing record
    View->>+Database: Update record
    Database-->>View: Return updated record
    View-->>Client: Return updated record data
    Note right of Client: Status Code: 200 - Ok

```

### Banco de dados
![Diagrama do banco de dados](images/database.png)

## Exemplo de payloads
...
