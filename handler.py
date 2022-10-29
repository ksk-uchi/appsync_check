import json
from logging import INFO, getLogger


logger = getLogger()
logger.setLevel(INFO)


def hello(event, context):
    logger.info(event)
    logger.info(context)

    return {"id": "xxxx", "name": "yyyy", "status": "zzzz"}

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
