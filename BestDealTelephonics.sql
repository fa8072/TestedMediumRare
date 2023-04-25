DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;

CREATE TABLE Users
(
	id serial PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	name varchar(50) NOT NULL,
	patronymic varchar(50) NOT NULL,
	login varchar(50) NOT NULL,
	password varchar(50) NOT NULL,
	role text NULL
);

INSERT INTO Users VALUES
(1, 'Кулешов', 'Александр', 'Михайлович', 'Admin', '12345', 'admin');

SELECT * FROM Users

INSERT INTO Users VALUES
(2, 'Жмышенко', 'Валерий', 'Альбертович', 'McBorov', '1234567890', NULL);

SELECT * FROM Users;

CREATE TABLE Products
(
    id serial PRIMARY KEY,
	title varchar(50) NOT NULL,
	storage integer NOT NULL,
	ram integer NOT NULL,
	cpu varchar(50) NOT NULL,
	mhz integer NOT NULL,
	price numeric(10, 2) NOT NULL
);

INSERT INTO Products VALUES
(1, "Xiaomi", 1024, 1024, "Mediatek", 2000, 8999);

INSERT INTO Products VALUES
(2, "Samsung", 1024, 1024, "Exyon", 2000, 9999);

INSERT INTO Products VALUES
(3, "Nokia", 1024, 1024, "Nokla", 2000, 4999);

INSERT INTO Products VALUES
(4, "Apple", 1024, 1024, "Appol", 2000, 89999);
