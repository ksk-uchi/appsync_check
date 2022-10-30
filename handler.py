import json
from logging import INFO, getLogger


logger = getLogger()
logger.setLevel(INFO)


def _for_subscription(event, context):
    logger.info("Subscription called")
    logger.info(event)
    logger.info(context)
    # raise Exception("you are not customer.")


def _switcher(event, key, dummy=""):
    return event["arguments"].get(key, dummy)


def hello(event, context):
    if event["info"]["parentTypeName"] == "Subscription":
        _for_subscription(event, context)
        return

    logger.info(event)
    logger.info(context)

    id_ = _switcher(event, "id", "xxxx")
    name_ = _switcher(event, "name", "yyyy")
    status_ = _switcher(event, "status", "zzzz")

    return {"id": id_, "name": name_, "status": status_}

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
