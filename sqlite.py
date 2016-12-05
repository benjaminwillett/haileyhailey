import sqlite3

DROP table Devices;
create table Devices(id INTEGER PRIMARY KEY, name varchar(64), ports smallint, vendor varchar(64));
