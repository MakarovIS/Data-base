CREATE TABLE hall (
	hall_id INTEGER PRIMARY KEY NOT NULL,
	hall_name VARCHAR(50));

CREATE TABLE actor (
	actor_id INTEGER PRIMARY KEY NOT NULL,
	actor_name_and_surname VARCHAR2(50),
	actor_date_of_birth DATE,
	actor_experience VARCHAR(2));

CREATE TABLE genre (
	genre_id INTEGER PRIMARY KEY NOT NULL
	genre_name VARCHAR(50));

CREATE TABLE spetacle (
	spetacle_id INTEGER PRIMARY KEY NOT NULL,
	spetacle_name VARCHAR(50),
	genre_id INTEGER,
	spetacle_length INTEGER);

CREATE TABLE employment_of_actors (
	contract_id INTEGER PRIMARY KEY NOT NULL,
	actor_id INTEGER,
	spetacle_id INTEGER,
	role_actor VARCHAR(50));

CREATE TABLE speech (
	speech_id INTEGER PRIMARY KEY NOT NULL,
	spetacle_id INTEGER,
	hall_id INTEGER,
	speech_date DATE,
	speech_time TIME);
	
CREATE TABLE category (
	category_id INTEGER PRIMARY KEY NOT NULL,
	hall_id INTEGER,
	category_row VARCHAR(3),
	category_price INTEGER);

CREATE TABLE ticket (
	ticket_id INTEGER PRIMARY KEY NOY NULL,
	category_id INTEGER,
	speech_id INTEGER,
	ticket_status BOOLEAN);