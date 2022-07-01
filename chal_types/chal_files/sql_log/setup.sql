ALTER USER 'root'@'localhost' IDENTIFIED BY 'secure';
CREATE USER 'sql'@'%' IDENTIFIED BY 'password';
CREATE DATABASE admin_site;
USE admin_site;
CREATE TABLE `users` (
    id int not null auto_increment,
    username text not null,
    password text not null,
    primary key (id)
);
GRANT ALL ON *.* TO 'sql'@'%';
FLUSH PRIVILEGES;