DROP DATABASE IF EXISTS cat_db;
CREATE DATABASE IF NOT EXISTS cat_db;
USE cat_db;
CREATE TABLE cats (id VARCHAR(10) PRIMARY KEY, name VARCHAR(50), origin VARCHAR(50), life_span DECIMAL(10, 2), weight DECIMAL(10, 2), description TEXT, image_url VARCHAR(255)); 
 INSERT INTO cats VALUES ("abys", "Abyssinian","Egypt",  14.5,  4.0, "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.", "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg")
 

/*  SELECT Country.Name, City.Name as Capital, Country.Continent , Country.Region, Country.Population FROM country  inner join city on country.Capital = city.ID; */
