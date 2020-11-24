CREATE DATABASE evergreen;
USE evergreen;
<<<<<<< HEAD
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
=======
CREATE TABLE Canal (
	id_canal INT(11) PRIMARY KEY AUTO_INCREMENT,
	nombre VARCHAR(20) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    tipo_destinatario VARCHAR(20) NOT NULL,
    fecha DATETIME
)
INSERT INTO canal(nombre, tipo, tipo_destinatario,fecha) VALUES ('Mensaje individual', 'SMS', 'Simple', '2020/07/15');
INSERT INTO canal(nombre, tipo, tipo_destinatario,fecha) VALUES ('Correo', 'Email', 'Grupo', '2020/06/22');
INSERT INTO canal(nombre, tipo, tipo_destinatario,fecha) VALUES ('Llamada', 'Central Telefonica', 'Simple', '2020/08/21');
>>>>>>> 4a410c7b4644a90b5a743415655b0d8f0820a488
