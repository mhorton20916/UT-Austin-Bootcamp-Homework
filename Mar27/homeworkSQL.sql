USE sakila;

-- 1a
SELECT first_name, last_name FROM actor;

-- 1b
SELECT concat(first_name,' ',last_name) AS 'Actor Name' FROM actor;

-- 2a
SELECT actor_id, first_name, last_name FROM actor
WHERE first_name='JOE';

-- 2b
SELECT first_name, last_name FROM actor
WHERE last_name LIKE '%GEN%';

-- 2c
SELECT first_name, last_name FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2d
SELECT country_id, country FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a
