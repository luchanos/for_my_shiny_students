"""Знать базовые команды для создания таблиц, типы полей (какие они бывают) и правила
построения простых запросов."""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
CREATE TABLE manufacturers (
manufacturer_id INT,
manufacturer_name TEXT,
country TEXT,
website TEXT
);

CREATE TABLE models (
model_id INT,
model_name TEXT,
manufacturer_code INT
);

CREATE TABLE sellers (
seller_id INT,
surname TEXT,
address TEXT,
phone TEXT,
website TEXT
)

CREATE TABLE goods (
good_id INT,
good_name TEXT
)

CREATE TABLE price_list (
position_id SERIAL,
seller_id INT,
manufacturer_id INT,
good_id INT,
model_id INT,
price INT
);

DROP TABLE manufacturers;
DROP TABLE models;
DROP TABLE sellers;
DROP TABLE goods;

INSERT INTO sellers VALUES (1, 'Свиридов', 'Москва', '666', 'www');
SELECT * FROM sellers;

INSERT INTO sellers VALUES (2, 'Иванов', 'Саратов', '555', 'www1'), (2, 'Петров', 'Омск', '777', 'www2');
SELECT surname AS govno FROM sellers;

SELECT * FROM sellers WHERE surname = 'Свиридов' OR website = 'www1';
SELECT * FROM sellers WHERE surname = 'Свиридов' AND website = 'www1';
SELECT * FROM sellers ORDER BY phone ASC LIMIT 1;
"""
