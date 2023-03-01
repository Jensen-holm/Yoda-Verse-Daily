def is_error(r) -> bool:
    """
    :param: r = requests response object
    :return: returns True if there is a 
    problem with the response and False
    if there is not a problem
    """
    if not 200 <= r.status_code <= 300:
        return True
    return False


def error_message(
        url: str, 
        status_code: int
    ) -> str:
    return f"{status_code} error in response body when requesting '{url}'"
