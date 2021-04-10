import requests
import json
import uuid


def get_processed_datetime(date_time, shift_value):
    print("Current Time => " + str(date_time))
    are_we_adding = False

    if shift_value[0] == "+":
        are_we_adding = True
    # Splitting Date Formats
    time_to_process = date_time[11:-1].split(":")

    time_to_change_by = shift_value[1:].split(":")

    new_minutes = 0
    new_seconds = 0

    if are_we_adding:
        new_hours = int(time_to_process[0]) + int(time_to_change_by[0])
        if len(time_to_change_by) > 1:
            new_minutes = int(time_to_process[1]) + int(time_to_change_by[1])
            if len(time_to_change_by) > 2:
                new_seconds = int(time_to_process[2]) + int(time_to_change_by[2])
                if new_seconds > 59:
                    new_minutes += 1
                    new_seconds -= 60
            if new_minutes > 59:
                new_hours += 1
                new_minutes -= 60
    else:
        new_hours = int(time_to_process[0]) - int(time_to_change_by[0])
        if len(time_to_change_by) > 1:
            new_minutes = int(time_to_process[1]) - int(time_to_change_by[1])
            if len(time_to_change_by) > 2:
                new_seconds = int(time_to_process[2]) - int(time_to_change_by[2])
                if new_seconds < 0:
                    new_minutes -= 1
                    new_seconds += 60
            if new_minutes < 0:
                new_hours -= 1
                new_minutes += 60

    new_datetime = date_time[:11] + format_time_to_two_digit(new_hours) + ":" + format_time_to_two_digit(
                                new_minutes) + ":" + format_time_to_two_digit(new_seconds) + "Z"
    return str(new_datetime)


def get_result_time_from_clock_time(current_clock_time, shift_value):
    are_we_adding = False

    if shift_value[0] == "+":
        are_we_adding = True

    # Splitting Date Formats
    time_to_process = current_clock_time.split(":")

    time_to_change_by = shift_value[1:].split(":")

    if time_to_process[1] is not None:
        new_minutes = time_to_process[1]

    if are_we_adding:
        new_hours = int(time_to_process[0]) + int(time_to_change_by[0])
        if len(time_to_change_by) > 1:
            new_minutes = int(time_to_process[1]) + int(time_to_change_by[1])
            if len(time_to_change_by) > 2:
                new_seconds = int(time_to_process[2]) + int(time_to_change_by[2])
                if new_seconds > 59:
                    new_minutes += 1
                    new_seconds -= 60
            if new_minutes > 59:
                new_hours += 1
                new_minutes -= 60
    else:
        new_hours = int(time_to_process[0]) - int(time_to_change_by[0])
        if len(time_to_change_by) > 1:
            new_minutes = int(time_to_process[1]) - int(time_to_change_by[1])
            if len(time_to_change_by) > 2:
                new_seconds = int(time_to_process[2]) - int(time_to_change_by[2])
                if new_seconds < 0:
                    new_minutes -= 1
                    new_seconds += 60
            if new_minutes < 0:
                new_hours -= 1
                new_minutes += 60

    new_datetime = format_time_to_two_digit(new_hours) + ":" + format_time_to_two_digit(new_minutes)
    return str(new_datetime)


def format_time_to_two_digit(number):
    if number is None:
        return "00"

    if len(str(number)) == 1:
        return "0" + str(number)

    return str(number)


def get_processed_string(previous_string, shift_value):
    print("Currently => " + "\"" + previous_string + "\"")

    string_date = previous_string.split(" ")
    final_string = ""

    x = 0
    for elem in string_date:
        if elem.find(":") > -1:
            string_date[x] = get_result_time_from_clock_time(elem, shift_value)
        x += 1

    for string_obj in string_date:
        if string_obj == string_date[0]:
            final_string = string_obj
        else:
            final_string = final_string + " " + string_obj

    # print(string_date[0] + " " + string_date[1])
    # print(string_date[-2] + " " + string_date[-1])
    if (string_date[0] + " " + string_date[1]) == "every day" and (string_date[-2] + " " + string_date[-1]) != "starting today":
        final_string = final_string + " starting today"

    print("Changed to => " + "\"" + final_string + "\"")
    return str(final_string)


def shift(token, task_item, shift_value):
    if task_item.due_string is not None:
        requests.post(
            "https://api.todoist.com/rest/v1/tasks/" + str(task_item.id),
            data=json.dumps({
                # "due_datetime": str(get_processed_datetime(task_item.due_datetime, shift_value)),
                # "recurring": bool(task_item.due_recurring),
                "due_string": str(get_processed_string(task_item.due_string, shift_value))
            }),

            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % token
            })
