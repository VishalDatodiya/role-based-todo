import time
from django.utils.deprecation import MiddlewareMixin


class APITimingMiddleware(MiddlewareMixin):
    """
    Middleware to calculate API response time
    """

    def process_request(self, request):
        # store start time
        request.start_time = time.time()

    # # ------------ For the header time will show in header

    # def process_response(self, request, response):
    #     try:
    #         # calculate elapsed time
    #         elapsed_time = time.time() - request.start_time
    #         response["X-Response-Time-ms"] = f"{elapsed_time * 1000:.2f}"
    #     except AttributeError:
    #         # in case request.start_time is missing
    #         response["X-Response-Time-ms"] = "N/A"

    #     return response

    # # ------------------------- Time in response it self ----------------------------

    def process_response(self, request, response):
        try:
            elapsed_time = time.time() - request.start_time
            response["X-Response-Time-ms"] = f"{elapsed_time * 1000:.2f}"

            if response.get("content-type") == "application/json":
                if hasattr(response, "data"):
                    response.data["response_time_ms"] = f"{elapsed_time * 1000:.2f}"
                    response._is_rendered = False  # re-render after modifying
                    response.render()
        except Exception:
            pass

        return response
