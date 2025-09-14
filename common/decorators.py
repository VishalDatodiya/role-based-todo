# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(
#             f"calling function {func.__name__} takes {end-start} time to execute.")
#         return res
#     return wrapper


import time
import functools
from rest_framework.response import Response


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)   # call the original view method
        end = time.time()
        elapsed = round((end - start) * 1000, 2)  # in ms

        # If the view already returned a DRF Response, inject response_time
        if isinstance(res, Response):
            # Add response_time safely
            res.data = dict(res.data)  # make mutable copy
            res.data["response_time_ms"] = elapsed
        return res
    return wrapper
