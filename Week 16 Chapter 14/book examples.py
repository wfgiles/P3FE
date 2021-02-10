CREATE TABLE People
(id INTEGER PRIMARY KEY, name TEXT INIQUE, retrieved INTEGER)

CREATE TABLE Follows
(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))

