CREATE DATABASE lab_db
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       LC_COLLATE = 'ru_RU.UTF-8'
       LC_CTYPE = 'ru_RU.UTF-8'
       TEMPLATE = template0;

CREATE ROLE lab_user WITH LOGIN PASSWORD 'root';

GRANT CONNECT ON DATABASE lab_db TO lab_user;

\connect lab_db

GRANT USAGE, CREATE ON SCHEMA public TO lab_user;
