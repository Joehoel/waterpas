DROP USER IF EXISTS 'user'@'localhost';
DROP DATABASE IF EXISTS waterpas;
CREATE DATABASE waterpas;
USE waterpas;
CREATE TABLE waarden (
    id INT NOT NULL AUTO_INCREMENT,
    pitch INT NOT NULL,
    roll INT NOT NULL,
    _time TIMESTAMP,
    PRIMARY KEY (id)
);
CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';
GRANT ALL PRIVILEGES ON *.* TO 'user'@localhost IDENTIFIED BY 'user';
