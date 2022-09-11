



CREATE DATABASE MountainDb;



CREATE TABLE Files (
    File_id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    File_name varchar(20) NOT NULL UNIQUE,
    File_n_columns int NOT NULL,
    File_n_rows int NOT NULL
);



CREATE TABLE DataPoints (
    DataPoint_id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
    DataPoint_elevation float NOT NULL,
    DataPoint_base_color varchar(20) NOT NULL,
    file_id int NOT NULL FOREIGN KEY REFERENCES Files(File_id)
);



