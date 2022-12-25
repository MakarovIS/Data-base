CREATE TABLE halls (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50));

CREATE TABLE posts (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50));

CREATE TABLE workers (
	id INTEGER PRIMARY KEY NOT NULL,
	surname VARCHAR(50),
	name VARCHAR(50),
	date_of_birth DATE,
	experience VARCHAR(2));

CREATE TABLE genres (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50));

CREATE TABLE spectacles (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50),
	genre_id INTEGER,
	lengths INTEGER);

CREATE TABLE employment_of_actors (
	id INTEGER PRIMARY KEY NOT NULL,
	worker_id INTEGER,
	spectacle_id INTEGER,
	role_actor VARCHAR(50));

CREATE TABLE speechs (
	id INTEGER PRIMARY KEY NOT NULL,
	spectacle_id INTEGER,
	hall_id INTEGER,
	date_and_time DATETIME);
	
CREATE TABLE ticket_price_categories (
	id INTEGER PRIMARY KEY NOT NULL,
	hall_id INTEGER,
	row VARCHAR(3),
	price INTEGER);

CREATE TABLE tickets (
	id INTEGER PRIMARY KEY NOT NULL,
	ticket_price_category_id INTEGER,
	speech_id INTEGER,
	status BOOLEAN);

INSERT INTO halls(id, name)
VALUES (1, 'Main'), (2, "Secondary");

INSERT INTO tickets(id, ticket_price_category_id, speech_id, status)
VALUES (1, 2, 3, FALSE);

INSERT INTO speechs(id, spectacle_id, hall_id, date_and_time)
VALUES (1, 2, 3, '2000-12-12 15:15:30');
