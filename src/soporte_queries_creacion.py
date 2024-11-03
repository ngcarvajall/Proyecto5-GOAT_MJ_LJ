tabla_lastdance_mj  = """
                                CREATE TABLE IF NOT EXISTS Tabla_2003 (
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
                                CREATE TABLE IF NOT EXISTS Tabla_2024 (
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

tabla_campeonatos_mj = """
                   CREATE TABLE IF NOT EXISTS Campeonatos_MJ (
                   Id_resultado int PRIMARY KEY,
                   resultado VARCHAR(20)
                   );
                   """


tabla_campeonatos_lj = """
                   CREATE TABLE IF NOT EXISTS Campeonatos_LJ (
                   Id_resultado int PRIMARY KEY,
                   resultado VARCHAR(20)
                   );
                   """

franquicias = """
                   CREATE TABLE IF NOT EXISTS Franquicias (
                   Franquicia varchar (50),
                   team_code varchar(10) PRIMARY KEY,
                   liga varchar(10),
                   Desde varchar(10),
                   Hasta varchar(10),
                   Anios int,
                   G int,
                   W int, 
                   L int,
                   W/L_perc float,
                   Plyfs int,
                   Div int,
                   Conf int,
                   Champ int,
                   );
                   """

Temp_mj = """
                   CREATE TABLE IF NOT EXISTS Temporadas_MJ (
                   Id_temporada int PRIMARY KEY,
                   Season varchar varchar(10),
                   team_code varchar(10),
                   CONSTRAINT fk_Franquicias FOREIGN KEY (team_code)
                        REFERENCES Franquicias (team_code) 
                   );"""

Temp_lj = """
                   CREATE TABLE IF NOT EXISTS Temporadas_LJ (
                   Id_temporada int PRIMARY KEY,
                   Season varchar varchar(10),
                   team_code varchar(10),
                   CONSTRAINT fk_Franquicias FOREIGN KEY (team_code)
                        REFERENCES Franquicias (team_code) 
                   );"""

temp_regular_mj = """
                   CREATE TABLE IF NOT EXISTS Temp_regular_MJ (
                   Id_temporada int,
                   team_code varchar(10),
                   player_age int,
                   GP int,
                   GS int,
                   Min float, 
                   FGM int,
                   FGA int,
                   FG_PCT float,
                   FG3M int,
                   FG3A int,
                   FG3_PCT float,
                   FTM int,
                   FTA int,
                   FT_PCT float,
                   OREB int,
                   DREB int,
                   REB int,
                   AST int,
                   STL int,
                   BLK int,
                   TOV int,
                   PF int, 
                   PTS int,
                   CONSTRAINT fk_Temporadas_MJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_MJ (Id_temporada) 
                   );"""

temp_regular_lj = """
                   CREATE TABLE IF NOT EXISTS Temp_regular_LJ (
                   Id_temporada int,
                   team_code varchar(10),
                   player_age int,
                   GP int,
                   W int,
                   L int,
                   W/L_PCT float,
                   Min float, 
                   FGM int,
                   FGA int,
                   FG_PCT float,
                   FG3M int,
                   FG3A int,
                   FG3_PCT float,
                   FTM int,
                   FTA int,
                   FT_PCT float,
                   OREB int,
                   DREB int,
                   REB int,
                   AST int,
                   TOV int,
                   STL int,
                   BLK int,
                   BLKA int,
                   PF int,
                   PFD int, 
                   PTS int,
                   PLUS_MINUS int,
                   CONSTRAINT fk_Temporadas_LJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_LJ (Id_temporada) 
                   );"""

playoffs_mj = """
                   CREATE TABLE IF NOT EXISTS Playoffs_MJ (
                   Id_temporada int,
                   player_age int,
                   team_code varchar(10),
                   G int,
                   GS int,
                   Min float, 
                   FGM float,
                   FGA float,
                   FG_PCT float,
                   FG3M float,
                   FG3A float,
                   FG3_PCT float,
                   FG2M float,
                   FG2A float,
                   FG2_PCT float, 
                   EFG_PCT float,
                   FTM float,
                   FTA float,
                   FT_PCT float,
                   OREB float,
                   DREB float,
                   REB float,
                   AST float,
                   STL float,
                   BLK float,
                   TOV float,
                   PF float, 
                   PTS float
                   Id_Resultado int,
                   CONSTRAINT fk_Temporadas_MJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_MJ (Id_temporada),
                   CONSTRAINT fk_Campeonatos_MJ FOREIGN KEY (Id_resultado)
                        REFERENCES Campeonatos_MJ (Id_resultado) 
                   );"""

playoffs_lj = """
                   CREATE TABLE IF NOT EXISTS Playoffs_LJ (
                   Id_temporada int,
                   player_age int,
                   team_code varchar(10),
                   G int,
                   GS int,
                   Min float, 
                   FGM int,
                   FGA int,
                   FG_PCT float,
                   FG3M float,
                   FG3A float,
                   FG3_PCT float,
                   FG2M float,
                   FG2A float,
                   FG2_PCT float, 
                   EFG_PCT float,
                   FTM float,
                   FTA float,
                   FT_PCT float,
                   OREB float,
                   DREB float,
                   REB float,
                   AST float,
                   STL float,
                   BLK float,
                   TOV float,
                   PF float, 
                   PTS float
                   Id_Resultado int,
                   CONSTRAINT fk_Temporadas_LJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_LJ (Id_temporada),
                   CONSTRAINT fk_Campeonatos_LJ FOREIGN KEY (Id_resultado)
                        REFERENCES Campeonatos_LJ (Id_resultado) 
                   );"""

salarios_mj = """
                   CREATE TABLE IF NOT EXISTS salarios_mj (
                   team_code varchar(10),
                   salario int,
                   salario_actual int,
                   Id_temporada int, 
                   CONSTRAINT fk_Temporadas_MJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_MJ (Id_temporada),
                   );"""

salarios_mj = """
                   CREATE TABLE IF NOT EXISTS salarios_lj (
                   team_code varchar(10),
                   salario int,
                   salario_actual int,
                   Id_temporada int, 
                   CONSTRAINT fk_Temporadas_LJ FOREIGN KEY (Id_temporada)
                        REFERENCES Temporadas_LJ (Id_temporada),
                   );"""