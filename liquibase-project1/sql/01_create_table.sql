--liquibase formatted sql
--changeset vaibhav:createTable1
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50)
);
