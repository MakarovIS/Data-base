CREATE TABLE halls (
	hall_id INTEGER PRIMARY KEY NOT NULL,
	hall_name VARCHAR(50));

CREATE TABLE posts (
	post_id INTEGER PRIMARY KEY NOT NULL,
	post_name VARCHAR(50));

CREATE TABLE workers (
	worker_id INTEGER PRIMARY KEY NOT NULL,
	worker_surname VARCHAR(50),
	worker_name VARCHAR(50),
	worker_date_of_birth DATE,
	worker_experience VARCHAR(2));

CREATE TABLE genres (
	genre_id INTEGER PRIMARY KEY NOT NULL,
	genre_name VARCHAR(50));

CREATE TABLE spetacles (
	spetacle_id INTEGER PRIMARY KEY NOT NULL,
	spetacle_name VARCHAR(50),
	genre_id INTEGER,
	spetacle_length INTEGER);

CREATE TABLE employment_of_actors (
	contract_id INTEGER PRIMARY KEY NOT NULL,
	worker_id INTEGER,
	spetacle_id INTEGER,
	role_actor VARCHAR(50));

CREATE TABLE speechs (
	speech_id INTEGER PRIMARY KEY NOT NULL,
	spetacle_id INTEGER,
	hall_id INTEGER,
	speech_date DATE,
	speech_time TIME);
	
CREATE TABLE categories (
	category_id INTEGER PRIMARY KEY NOT NULL,
	hall_id INTEGER,
	category_row VARCHAR(3),
	category_price INTEGER);

CREATE TABLE tickets (
	ticket_id INTEGER PRIMARY KEY NOT NULL,
	category_id INTEGER,
	speech_id INTEGER,
	ticket_status BOOLEAN);