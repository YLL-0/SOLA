

CREATE TABLE grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    grade FLOAT NOT NULL,
    date DATE NOT NULL
);