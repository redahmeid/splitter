import json


def hours(event, context):

    query_parameters = event["queryStringParameters"] if 'queryStringParameters' in event else None
    print(query_parameters)
    value = query_parameters["value"] if query_parameters is not None and 'value' in query_parameters else None
    hours = ''
    if(value!=''): hours = convert_to_hours(value)

    response = {"statusCode": 200, "body": json.dumps(hours)}

    return response

def days(event, context):

    query_parameters = event["queryStringParameters"] if 'queryStringParameters' in event else None
    print(query_parameters)
    value = query_parameters["value"] if query_parameters is not None and 'value' in query_parameters else None
    hours = ''
    if(value!=''): hours = convert_to_days(value)

    response = {"statusCode": 200, "body": json.dumps(hours)}

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

def convert_to_days(time_str):
    parts = time_str.split()
    total_days = 0
    for part in parts:
        if part[-1] == 'w':
            total_days += int(part[:-1]) * 7
        elif part[-1] == 'd':
            total_days += int(part[:-1])
        elif part[-1] == 'h':
            total_days += int(part[:-1]) / 24
    return total_days




