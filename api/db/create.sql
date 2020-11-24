CREATE DATABASE evergreen;
USE evergreen;
CREATE TABLE mensaje (
id_men int(255) primary key auto_increment,
asunto varchar(200) not null,
cuerpo varchar(200) not null,
remitente varchar(200) not null,
destinatario varchar(200) not null,
adjunto varchar(200),
canal varchar(200) not null,
estado varchar(200)
);
INSERT INTO mensaje(asunto, cuerpo, remitente,destinatario, canal, estado) VALUES ('Mensaje URGENTE', 'Es necesaria su presencia en la Oficina principal', 'jefe@jefe.com', 'bademployee@bademployee.com','Correo','Enviado');
