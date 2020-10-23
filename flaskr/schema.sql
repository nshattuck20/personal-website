DROP TABLE IF EXISTS post; 

CREATE TABLE post(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	author_id INTEGER NOT NULL, 
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
	title TEXT NOT NULL, 
	body TEXT NOT NULL

); 

