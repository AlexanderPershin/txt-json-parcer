def conv_int(id):
    # Try to convert to int
    try:
        res = int(id)
        # If successfull - return success: True and value: res
        return (True, res)
    except ValueError:
        res = id
        return (False, res)
