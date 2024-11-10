-- Temporadas ganadoras de LeBron en Playoffs
SELECT id_temporada, player_age, team_code, fg_pct, min, pts
FROM campeonatos_lj cl
INNER JOIN playoffs_lj pl 
ON cl.id_resultado = pl.id_resultado 
WHERE pl.id_resultado = 1
;
-- Temporadas ganadoras MJ
SELECT id_temporada, player_age, team_code, fg_pct, min, pts
FROM campeonatos_mj cm 
INNER JOIN playoffs_mj pm 
ON cm.id_resultado = pm.id_resultado 
WHERE pm.id_resultado = 1;

-- Salario histórico LJ
SELECT sl.team_code, salario, salario_actual, sl.id_temporada, tl.season 
FROM salarios_lj sl 
INNER JOIN temporadas_lj tl 
ON sl.id_temporada = tl.id_temporada 
ORDER BY sl.id_temporada ASC ;

-- Salario acumulado LJ
SELECT sum(salario_actual), team_code, count(id_temporada) 
FROM salarios_lj sl 
GROUP BY team_code;

-- Salario histórico MJ
SELECT *
FROM salarios_mj sm 
ORDER BY id_temporada ASC ;

-- Salario acumulado MJ
SELECT sum(salario_actual), team_code, count(id_temporada) 
FROM salarios_mj sm 
GROUP BY team_code;

-- Ultima temporada de LeBron (stats) y tabla
SELECT tl.id_temporada, tl.team_code, player_age, gp, w,l, round(min), reb, ast, stl, blk, pts
FROM temp_regular_lj trl 
INNER JOIN temporadas_lj tl 
ON trl.id_temporada = tl.id_temporada 
WHERE tl.season = '2023-24';

-- Ultima temporada y su impacto en el equipo
SELECT tl.id_temporada, tl.team_code,t.posicion ,player_age, gp AS partidos_jugados, t.partidos ,trl.w AS victorias_conseguidas, t.victorias,trl.l AS derrotas_sufridas, t.derrotas , round(min) AS minutos_jugados, reb, ast, stl, blk, pts
FROM temp_regular_lj trl 
INNER JOIN temporadas_lj tl 
ON trl.id_temporada = tl.id_temporada 
INNER JOIN franquicias f 
ON tl.team_code = f.team_code 
INNER JOIN tabla_2024 t 
ON f.team_code = t.team_code 
WHERE tl.season = '2023-24' ;

-- Ultima temporada de MJ y su impacto en el equipo
SELECT tm.id_temporada, trm.team_code,t.partidos,  player_age, trm.gp AS partidos_jugados, t.partidos, trm.min AS minutos_jugados, trm.reb, trm.ast, trm.stl, trm.blk, trm.pts, t.victorias, t.derrotas 
FROM temporadas_mj tm 
INNER JOIN temp_regular_mj trm 
ON tm.id_temporada = trm.id_temporada 
INNER JOIN franquicias f 
ON f.team_code = tm.team_code 
INNER JOIN tabla_2003 t 
ON f.team_code = t.team_code 
WHERE tm.season = '2002-03';

-- Union desde lo que aportó a franquicia hasta resultado de campeonato/tempordas de campeonato LJ
SELECT *
FROM temp_regular_lj trl 
INNER JOIN temporadas_lj tl 
ON trl.id_temporada = tl.id_temporada 
INNER JOIN franquicias f 
ON tl.team_code = f.team_code 
INNER JOIN tabla_2024 t 
ON f.team_code = t.team_code 
INNER JOIN playoffs_lj pl 
ON tl.id_temporada = pl.id_temporada 
WHERE pl.id_resultado = 1
ORDER BY tl.id_temporada ASC ;


-- Temporadas de campeonatos MJ
SELECT *
FROM temp_regular_mj trm 
INNER JOIN temporadas_mj tm 
ON trm.id_temporada = tm.id_temporada 
INNER JOIN franquicias f 
ON tm.team_code = f.team_code 
INNER JOIN tabla_2003 t2 
ON f.team_code = t2.team_code 
INNER JOIN playoffs_mj pm 
ON tm.id_temporada = pm.id_temporada 
WHERE pm.id_resultado = 1
ORDER BY tm.id_temporada ASC ;

-- Títulos por franquicia MJ
SELECT *
FROM franquicias f 
WHERE team_code in ('CHI', 'WAS') ;

-- Títulos por franquicia LJ
SELECT *
FROM franquicias f
WHERE team_code IN ('CLE', 'MIA', 'LAL');

-- Partidos LeBron por equipo y sus puntos
SELECT team_code, sum(gp) AS partidos, count(id_temporada) AS temporadas, sum(pts) AS puntos_aportados, round(avg(gp))
FROM temp_regular_lj trl 
GROUP BY team_code ;

-- Partidos MJ por equipo y sus puntos
SELECT team_code, sum(gp) partidos, count(id_temporada) AS temporadas, sum(pts) AS puntos_aportados, round(avg(gp))
FROM temp_regular_mj trm
GROUP BY team_code ;

SELECT *
FROM temp_regular_lj trl ;

-- Campeonatos por franquicia y lo que aportó LJ
SELECT tl.team_code, count(pl.id_resultado) AS campeonatos, f.champ 
FROM temp_regular_lj trl 
INNER JOIN temporadas_lj tl 
ON trl.id_temporada = tl.id_temporada 
INNER JOIN franquicias f 
ON tl.team_code = f.team_code 
INNER JOIN tabla_2024 t 
ON f.team_code = t.team_code 
INNER JOIN playoffs_lj pl 
ON tl.id_temporada = pl.id_temporada
WHERE pl.id_resultado = 1
GROUP BY tl.team_code, f.champ ;

-- Cantidad de puntos en temporada regular para cada equipo
SELECT *
FROM playoffs_lj pl  ;

-- Campeonatos por franquicia y lo que aportó MJ
SELECT 
    tm.team_code, 
    count(pm.id_resultado) AS campeonatos, 
    f.champ 
FROM 
    temp_regular_mj trm 
INNER JOIN 
    temporadas_mj tm ON trm.id_temporada = tm.id_temporada 
INNER JOIN 
    franquicias f ON tm.team_code = f.team_code 
INNER JOIN 
    tabla_2003 t ON f.team_code = t.team_code 
INNER JOIN 
    playoffs_mj pm ON tm.id_temporada = pm.id_temporada 
WHERE 
    pm.id_resultado = 1 
GROUP BY 
    tm.team_code, f.champ;

-- Trayectoria en playoffs de LJ finales, runner-up y campenato
SELECT 
    team_code,
    COUNT(CASE WHEN id_resultado = 0 THEN 1 END) AS contendiente,
    COUNT(CASE WHEN id_resultado = 1 THEN 1 END) AS campeonato,
    COUNT(CASE WHEN id_resultado = 2 THEN 1 END) AS finalista
FROM 
    playoffs_lj
GROUP BY 
    team_code;

-- Trayectoria en playoffs de MJ runner-up y campeonato
SELECT team_code,
	count(CASE WHEN id_resultado = 0 THEN 1 end) AS contendiente,
	count(CASE WHEN id_resultado = 1 THEN 1 end) AS campeonato
FROM playoffs_mj pm 
GROUP BY team_code ;

-- Est temp_regular LJ

SELECT tl.id_temporada , tl.team_code, gp, w, l, w_l_pct , round(min) , fg_pct , reb, ast, blk, pts
FROM temp_regular_lj trl 
INNER JOIN temporadas_lj tl 
ON trl.id_temporada = tl.id_temporada 
;


-- Est playoffs LJ
SELECT id_temporada, team_code,g, min, fg_pct , reb, ast, stl, blk, pts, id_resultado 
FROM playoffs_lj pl ;

-- Est playoffs MJ
SELECT id_temporada , team_code, g, min, fg_pct , reb, ast , stl, blk, pts, id_resultado 
FROM playoffs_mj pm ;


-- Est temp_regular MJ
SELECT tm.id_temporada, tm.team_code , gp , round(min) fg_pct, reb, ast, blk, pts
FROM temp_regular_mj trm 
INNER JOIN temporadas_mj tm 
ON trm.id_temporada = tm.id_temporada 
;

SELECT *
FROM temporadas_lj tl ;
SELECT *
FROM playoffs_lj pl 
INNER JOIN 