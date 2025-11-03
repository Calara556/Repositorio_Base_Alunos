CREATE TABLE IF NOT EXISTS medico (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        VACHAR(250),
    crm         VACHAR(100)
);

CREATE TABLE IF NOT EXISTS paciente (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nome        VACHAR(250),
    cpf         VACHAR(11)
);

CREATE TABLE IF NOT EXISTS consulta (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    idMedico        INTEGER,
    idPaciente      INTEGER,
    dataConsulta    DATE,
    FOREIGN KEY (idMedico) REFERENCES medico (id),
    FOREIGN KEY (idPaciente) REFERENCES paciente(id)
);

INSERT INTO medico (nome, crm) VALUES
('Ana Cláudia Michels', '1234.5678.910'),
('Adrina de Oliveira Melo', '1234.5678.910'),
('Oswaldo Cruz', '1234.5678.910'),
('Carlos Chagas', '1234.5678.910'),
('Zilda Arns', '1234.5678.910'),
('Adolfo Lutz', '1234.5678.910'),
('Nise da Silveira', '1234.5678.910'),
('Drauzio Varella', '1234.5678.910'),
('José Osmar Medina Pestana', '1234.5678.910'),
('José Pedro da Silva', '1234.5678.910');

INSERT INTO paciente (nome, cpf) VALUES
('Márcio', 'XXX.XXX.XXX-XX'),
('Valdete', 'XXX.XXX.XXX-XX'),
('Cleiton', 'XXX.XXX.XXX-XX'),
('Lázaro', 'XXX.XXX.XXX-XX'),
('Geovanna', 'XXX.XXX.XXX-XX'),
('Ana Clara', 'XXX.XXX.XXX-XX'),
('Amanda', 'XXX.XXX.XXX-XX'),
('Pyetra', 'XXX.XXX.XXX-XX'),
('Camylly', 'XXX.XXX.XXX-XX'),
('Juliana', 'XXX.XXX.XXX-XX'),
('Joana', 'XXX.XXX.XXX.-XX');
INSERT INTO consulta
(idMedico, idPaciente, dataConsulta) VALUES
(1, 4, date('now')),
(2, 2, date('now')),
(2, 3, date('now'));

