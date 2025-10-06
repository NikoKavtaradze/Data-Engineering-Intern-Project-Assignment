-- This SQL file creates the stock_data database and tables for AAPL, GOOG, and MSFT
CREATE DATABASE IF NOT EXISTS stock_data;
SHOW DATABASES;

USE stock_data;

CREATE TABLE IF NOT EXISTS GOOG (
	date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    adjusted_close FLOAT,
    volume INT,
    daily_change_percentage FLOAT
);
CREATE TABLE IF NOT EXISTS MSFT (
	date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    adjusted_close FLOAT,
    volume INT,
    daily_change_percentage FLOAT
);
CREATE TABLE IF NOT EXISTS AAPL (
	date DATE,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    adjusted_close FLOAT,
    volume INT,
    daily_change_percentage FLOAT
);

SHOW TABLES;


-- Little Changes:) (added two columns into my tables)
USE stock_data;

ALTER TABLE AAPL ADD COLUMN dividend FLOAT;
ALTER TABLE AAPL ADD COLUMN split_coefficient FLOAT;
ALTER TABLE GOOG ADD COLUMN dividend FLOAT;
ALTER TABLE GOOG ADD COLUMN split_coefficient FLOAT;
ALTER TABLE MSFT ADD COLUMN dividend FLOAT;
ALTER TABLE MSFT ADD COLUMN split_coefficient FLOAT;
