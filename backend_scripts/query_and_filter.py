def query(output):
    """
    Returns: an SQL query string that filters and retrieves data from the 
    database based on the user's selections.

    The query function processes the user's selections from the argument output, 
    containing a list of ipywidgets.Widget objects:
    1. programs: A SelectMultiple widget containing the selected program flags
       (e.g., NPDES_FLAG, AIR_FLAG, RCRA_FLAG).
    2. active: A Checkbox widget indicating whether to filter results by active
       facilities.
    3. naics: A Text widget containing the input NAICS codes, separated by commas.

Example:
    selections = [programs, active, naics] # list of ipywidgets.Widget objects
    squery = query(selections)
    > squery now contains an SQL query string based on the user's selections
    """
    programs = output[0]
    active = output[1]
    naics = output[2]
    sql_string = '(('
    pgms = ''
    if len(programs.value) > 0:
        for pgm in programs.value:
            pgms += "\""+pgm+"\" = \'Y\' or "
    pgms = pgms[:-4]
    sql_string += pgms


    # Filter by active
    if active.value:
        sql_string += ' and "FAC_ACTIVE_FLAG" = \'Y\')'
    else:
        sql_string += ')'

    # Filter by NAICS
    pgm_key = {"NPDES_FLAG": "CWA_NAICS", "AIR_FLAG": "CAA_NAICS", "RCRA_FLAG": "RCRA_NAICS"}
    naics_string = ' and ('
    for n in naics.value.replace(" ", "").split(","):
        if len(n) == 6:
            naics_string += '"FAC_NAICS_CODES" like \'%'+n+'%\' or '
            for pgm in programs.value:
                naics_string += '"'+pgm_key[pgm]+'" like \'%'+n+'%\' or '
        else:
            missing = 6 - len(n)
            wilds = "%" * missing
            naics_string += '"FAC_NAICS_CODES" like \' %'+n+''+wilds+'\' or '
            naics_string += '"FAC_NAICS_CODES" like \''+n+''+wilds+'\' or '
            for pgm in programs.value:
                naics_string += '"'+pgm_key[pgm]+'" like \' %'+n+''+wilds+'\' or '
                naics_string += '"'+pgm_key[pgm]+'" like \''+n+''+wilds+'\' or '
    
    # String together
    naics_string = naics_string[:-4]
    naics_string += "))"
    sql_string = sql_string + naics_string
    return sql_string
