

def return_result_and_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return {
                "result": result,
                "error": []
            }
        except Exception as e:
            return {
                "result": False,
                "error": [e]
            }
    return wrapper





