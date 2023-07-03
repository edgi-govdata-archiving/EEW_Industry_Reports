import ipywidgets 

def make_selections():
    """
    Creates and displays ipywidgets for selecting program flags,
    filtering by active facilities, and inputting NAICS codes. 
    Returns: a list containing the three ipywidgets objects created.

    The make_selections function creates and displays three ipywidgets:
    1. programs: A SelectMultiple widget that allows users to choose from
       three available program flags: NPDES_FLAG, AIR_FLAG, and RCRA_FLAG.
    2. active: A Checkbox widget that allows users to filter results by active
       facilities. When checked, only active facilities will be included in the
       results.
    3. naics: A Text widget that allows users to input NAICS codes separated by
       commas (e.g., 2111,213111,213112). Users can input multiple NAICS codes
       for filtering.

    Example:
        selections = make_selections()
        > Displays ipywidgets for user interaction
        > selections now contains a list of the three ipywidgets objects
    """
    programs = ipywidgets.SelectMultiple(
        options=['NPDES_FLAG', 'AIR_FLAG', 'RCRA_FLAG'],
        description='Programs',
        disabled=False
    )
    active = ipywidgets.Checkbox(
        value=False,
        description='Only active facilities?',
        disabled=False
    )
    naics = ipywidgets.Text(
        value='',
        placeholder='Enter NAICS codes here, separated with a comma', #2111,213111,213112
        description='NAICS codes',
        disabled=False
    )
    display(programs, active, naics)
    output = [programs, active, naics]

    return output


