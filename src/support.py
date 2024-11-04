import pandas as pd

def extraer_datos_equipos_df(responsa, num_equipos):
    """
    Extrae datos de equipos desde un diccionario `responsa` y los organiza en un DataFrame de pandas.

    Parameters:
    ----------
    responsa : dict
        Diccionario que contiene los datos de los equipos en la clave 'standings'.
    num_equipos : int, optional
        Número de equipos a extraer (por defecto es 30).

    Returns:
    -------
    pd.DataFrame
        DataFrame donde cada fila representa un equipo con las columnas:
        'Equipo', 'Nombre_comun', 'Codigo_equipo', 'Posicion', 'Partidos', 
        'Victorias', 'Derrotas', y 'Porcentaje_vic'.

    Example:
    -------
    >>> df = extraer_datos_equipos_df(responsa)
    >>> print(df.head())
    """
    lista_diccionario = []
    for i in range(num_equipos):
        nombre_equipo = responsa['standings'][8]['rows'][i]['team']['name']
        nombre_corto = responsa['standings'][8]['rows'][i]['team']['shortName']
        name_code = responsa['standings'][8]['rows'][i]['team']['nameCode']
        position = responsa['standings'][8]['rows'][i]['position']
        partidos = responsa['standings'][8]['rows'][i]['matches']
        victorias = responsa['standings'][8]['rows'][i]['wins']
        derrotas = responsa['standings'][8]['rows'][i]['losses']
        per_vic = responsa['standings'][8]['rows'][i]['percentage']
        
        diccionario = {
            'Equipo': nombre_equipo,
            'Nombre_comun': nombre_corto,
            'Codigo_equipo': name_code,
            'Posicion': position,
            'Partidos': partidos,
            'Victorias': victorias,
            'Derrotas': derrotas,
            'Porcentaje_vic': per_vic
        }
        
        lista_diccionario.append(diccionario)
    
    # Convertir la lista de diccionarios a DataFrame
    df = pd.DataFrame(lista_diccionario)
    return df
