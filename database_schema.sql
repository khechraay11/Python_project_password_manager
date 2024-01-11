-- database_schema.sql

-- Table: t_encrypt
CREATE TABLE t_encrypt (
    IV VARBINARY(64) NULL,
    data VARBINARY(64) NULL
);

-- Table: t_data
CREATE TABLE t_data (
    website VARCHAR(40) NULL,
    username VARCHAR(40) NULL,
    psswrd VARBINARY(64) NULL
);
