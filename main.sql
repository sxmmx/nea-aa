CREATE TABLE Users(
  User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  User_name varchar(50) NOT NULL,
  User_password varchar(10) NOT NULL
);

INSERT INTO Users (User_ID, User_name, User_password) VALUES (?, ?, ?);
