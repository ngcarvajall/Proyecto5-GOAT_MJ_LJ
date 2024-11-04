SELECT * 
FROM campeonatos_lj cl
INNER JOIN playoffs_lj pl 
ON cl.id_resultado = pl.id_resultado 
WHERE pl.id_resultado = 1
;

SELECT *
FROM temporadas_lj tl ;

SELECT *
FROM temporadas_mj tm ;