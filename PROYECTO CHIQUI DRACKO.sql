create table Cliente(
Nombre varchar not null,
Cedula varchar(10) not null,
Direccion varchar not null,
Ciudad varchar(50) not null,
PRIMARY KEY(Cedula)	
);

COPY Cliente(Nombre, Cedula, Direccion, Ciudad)
FROM 'D:\PROYECTO ING DE DATOS\cliente.csv' DELIMITER ';' CSV HEADER;


create table Producto(
Nombre varchar not null,
Precio numeric(10,2) not null,
Costo_envio_flex numeric(10,2),
Costo_envio_colecta numeric(10,2),	
Utilidad_total varchar not null,
Rentabilidad varchar(4) not null,
PRIMARY KEY(Nombre)	
);

COPY Producto(Nombre, Precio, Costo_envio_flex, Costo_envio_colecta, Utilidad_total, Rentabilidad)
FROM 'D:\PROYECTO ING DE DATOS\productos.csv' DELIMITER ';' NULL '' CSV HEADER;


create table Empleado(
Cedula varchar(10) not null,
Nombre varchar(40) not null,
Fecha_nacimiento date not null,
Id_cuenta varchar(10),	
PRIMARY KEY(Cedula)	
);

INSERT INTO Empleado values('5524016532', 'Yovani Calero', '24/03/1985','2555563480');
INSERT INTO Empleado values('1001342028', 'Silvia Daniela Lotero Ruiz','20/01/2001','2555520256');
INSERT INTO Empleado values('1010984753', 'Felipe Gallego','13/08/1999','2555510098');
INSERT INTO Empleado values('1004857624', 'Sebastián Calero','11/11/2000','255559871');
INSERT INTO Empleado values('1054109835', 'Edison Gonzalez','28/04/1998','2555594862');
INSERT INTO Empleado values('1098334930', 'Edwin Polo','15/04/2000','2555594862');


create table Registro_compra(
Numero_compra varchar(40) not null,
Fecha_venta varchar not null,
Varios_productos varchar(2),
Unidades integer not null,
Valor_total varchar not null,
Nombre_producto varchar not null,
Cedula_cliente varchar(10) not null,
PRIMARY KEY(Numero_compra),
FOREIGN KEY(Cedula_cliente) references cliente,
FOREIGN KEY(Nombre_producto) references producto	
);


COPY Registro_compra(Numero_compra, Fecha_venta, Varios_productos, Unidades, Valor_total, Nombre_producto, Cedula_cliente)
FROM 'D:\PROYECTO ING DE DATOS\Registro_compra.csv' DELIMITER ';' CSV HEADER;

create table Registro_publicacion(
SKU varchar,
Cod_publicacion varchar(15) not null,
Nombre_Producto varchar not null,	
Cedula_Empleado varchar(10) not null,
PRIMARY KEY(Cod_publicacion),
FOREIGN KEY(Cedula_Empleado) references empleado,
FOREIGN KEY(Nombre_Producto) references producto
);

COPY Registro_publicacion(SKU, Cod_publicacion, Nombre_Producto, Cedula_Empleado)
FROM 'D:\PROYECTO ING DE DATOS\Registro_publicacion.csv' DELIMITER ';' CSV HEADER;



create table Registro_envio(
Nombre_producto varchar not null,
Forma_entrega varchar not null,
Transportadora varchar(40) not null,
Numero_seguimiento varchar(25) not null,
PRIMARY KEY(Numero_seguimiento),
FOREIGN KEY(Nombre_producto)references Producto	
);

COPY Registro_envio(Nombre_Producto, Forma_entrega, Transportadora, Numero_Seguimiento)
FROM 'D:\PROYECTO ING DE DATOS\Registro_envio.csv' DELIMITER ';' CSV HEADER;


SELECT*
FROM registro_publicacion


