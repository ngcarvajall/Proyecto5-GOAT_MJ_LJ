tabla_lastdance_mj  = """
                                CREATE TABLE Tabla_2003 (
                                Equipo varchar(50),
                                Nombre_comun varchar(50),
                                Codigo_equipo varchar(10),
                                Posicion int unique not null,
                                Partidos int,
                                Victorias int, 
                                Derrotas int
                                Porcentaje_vic float
                                );
                                """

tabla_lastdance_lj  = """
                                CREATE TABLE Tabla2024 (
                                Equipo varchar(50),
                                Nombre_comun varchar(50),
                                Codigo_equipo varchar(10),
                                Posicion int unique not null,
                                Partidos int,
                                Victorias int, 
                                Derrotas int
                                Porcentaje_vic float
                                );
                                """

tabla_tipo_hospi = """
                   CREATE TABLE TipoHospitalizacion (
                   id SERIAL PRIMARY KEY,
                   tipo_hospitalizacion VARCHAR(20) NULL UNIQUE
                   );
                   """