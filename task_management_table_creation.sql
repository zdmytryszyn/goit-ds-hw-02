
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);


DROP TABLE IF EXISTS status;
CREATE TABLE status
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE
);


DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(50),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
      ON DELETE SET NULL
      ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

