-- Active: 1728520757702@@127.0.0.1@3306
-- 01. Querying data
SELECT LastName FROM employees;

SELECT LastName, FirstName From employees;

SELECT * FROM employees;

SELECT FirstName AS '아름' FROM employees;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;
-- 02. Sorting data
SELECT
  FirstName
FROM 
  employees
ORDER BY
  FirstName;

SELECT
  FirstName
FROM 
  employees
ORDER BY
  FirstName DESC;

SELECT
  Country,
  City
FROM
  customers
ORDER BY
  Country DESC,
  City
;

SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT ReportsTo FROM employees ORDER BY ReportsTo;

-- 03. Filtering data
SELECT Country FROM customers ORDER BY Country;
SELECT DISTINCT Country FROM customers ORDER BY Country;
SELECT LastName, FirstName, City FROM customers WHERE City='Prague';
SELECT 
  LastName, FirstName, City 
FROM 
  customers 
WHERE 
  City!='Prague'
;

SELECT LastName, FirstName, Company, Country FROM customers WHERE Company ISNULL AND Country='USA';
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company ISNULL OR Country='USA';
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 100000 AND 500000;
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 100000 AND 500000 ORDER BY Bytes;
SELECT LastName, FirstName, Country FROM customers WHERE Country IN ('Canada', 'Germany', 'France');
SELECT LastName, FirstName, Country FROM customers WHERE Country NOT IN ('Canada', 'Germany', 'France');
SELECT LastName, FirstName FROM customers WHERE LastName LIKE '%son';
SELECT LastName, FirstName FROM customers WHERE FirstName LIKE '___a';
-- 04. Grouping data
SELECT Composer, AVG(Bytes) FROM tracks GROUP BY Composer ORDER BY AVG(Bytes) DESC;
SELECT 
  Composer, 
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM 
  tracks 
GROUP BY 
  Composer
HAVING
  avgOfMinute < 10
;
