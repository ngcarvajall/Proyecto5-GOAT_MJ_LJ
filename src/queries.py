
query_EDA_5 = """
SELECT sum(salario_actual), team_code, count(id_temporada) 
FROM salarios_lj sl 
GROUP BY team_code;
"""

