from rest_framework.response import Response
from rest_framework import status


def service_wrapper(action):
    try:
        ActionResult, status_code = action()
        return Response(ActionResult, status=status_code)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
