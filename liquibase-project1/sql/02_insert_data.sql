--liquibase formatted sql
--changeset vaibhav:insertData1
INSERT INTO employee (id, name, role) VALUES (1, 'John Doe', 'Manager');
INSERT INTO employee (id, name, role) VALUES (2, 'Jane Smith', 'Engineer');
