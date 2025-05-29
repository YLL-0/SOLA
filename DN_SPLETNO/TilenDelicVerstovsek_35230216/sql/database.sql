CREATE TABLE grades (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unikatni identifikator zapisa, samodejno se povečuje
    student_name VARCHAR(100) NOT NULL, -- Ime študenta, obvezen podatek
    subject VARCHAR(100) NOT NULL, -- Predmet, obvezen podatek
    grade FLOAT NOT NULL, -- Ocena, obvezen podatek, shranjen kot decimalno število
    date DATE NOT NULL -- Datum ocene, obvezen podatek
);