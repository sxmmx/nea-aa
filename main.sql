CREATE TABLE Users(
  User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  User_name varchar(50) NOT NULL,
  User_password varchar(10) NOT NULL
);

INSERT INTO Users (User_ID, User_name, User_password) VALUES (?, ?, ?);

CREATE TABLE Results(
  Result_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  User_name varchar(50) NOT NULL,
  Score INTEGER NOT NULL
);

CREATE TABLE Questions(
  Question_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Choice1 varchar(50) NOT NULL,
  Choice2 varchar(50) NOT NULL,
  Choice3 varchar(50) NOT NULL,
  Answer varchar(50) NOT NULL
);
