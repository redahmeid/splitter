import json


def hello(event, context):

    query_parameters = event["queryStringParameters"] if 'queryStringParameters' in event else None
    print(query_parameters)
    value = query_parameters["value"] if query_parameters is not None and 'value' in query_parameters else None
    

    response = {"statusCode": 200, "body": json.dumps(convert_to_hours(value))}

    return response

def convert_to_hours(time_string):
    time_units = time_string.split()
    hours = 0
    for time_unit in time_units:
        if time_unit.endswith('w'):
            hours += int(time_unit[:-1]) * 7 * 24
        elif time_unit.endswith('d'):
            hours += int(time_unit[:-1]) * 24
        elif time_unit.endswith('h'):
            hours += int(time_unit[:-1])
    return hours

