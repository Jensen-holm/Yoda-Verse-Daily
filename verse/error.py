def is_error(r) -> bool:
    """
    :param: r = requests response object
    :return: returns True if there is a 
    problem with the response and False
    if there is not a problem
    """
    code = r.status_code
    if not 200 <= code <= 300:
        return True
    return False
