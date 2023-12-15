
-- CREATE TABLE ranking (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );
--
-- INSERT INTO ranking (name) VALUES ('A'), ('B'), ('C'), ('D');

-- Criação da tabela de clientes
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
-- Criação da tabela de status e tickets

-- CREATE TABLE ticketStatus (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(20) UNIQUE
-- );
-- INSERT INTO ticketStatus (name) VALUES ('pending'), ('review'), ('solved'), ('closed');

CREATE TABLE ticket (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    status INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    closed_by_id INTEGER
--     FOREIGN KEY (status_id) REFERENCES ticketStatus(id) ON DELETE CASCADE
);
-- Criação da tabela de analistas de suporte
CREATE TABLE support (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    ranking VARCHAR(1) NOT NULL,
    ticket INTEGER,
    FOREIGN KEY (ticket) REFERENCES ticket(id) ON DELETE CASCADE
);



-- Exemplo de inserção de dados iniciais
INSERT INTO customer (name, email) VALUES
    ('Cliente 1', 'cliente1@email.com'),
    ('Cliente 2', 'cliente2@email.com');

INSERT INTO support (name, email, ranking) VALUES
    ('Analista 1', 'analista1@email.com', 'A'),
    ('jose', 'jose1@email.com', 'C'),
    ('Analista 2', 'analista2@email.com', 'A');

INSERT INTO ticket (title, description, status, closed_by_id) VALUES
    ('Problema 1', 'Descrição do problema 1', 1, NULL),
    ('Problema 2', 'Descrição do problema 2', 1, NULL);
