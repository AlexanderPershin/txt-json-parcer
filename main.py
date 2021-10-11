import json

from helpers.is_part_of_q import is_part_of_q
from helpers.to_dict import to_dict
from helpers.split_questions import split_questions


def read_file(name='master_test.txt'):
    with(open(name, 'r', encoding='utf-8') as f):
        content = f.read()
        return content


def clear_lines(content):
    for i in range(0, len(content)):
        content[i] = content[i].lstrip()

    return content


def print_by_lines(content):
    for i in range(0, len(content)):
        print(content[i], "\n")


questions = read_file()
q_array = questions.split("\n")
if(q_array[0] == 'QUESTIONS:'):
    del q_array[0]

# Remove spaces from start/end of each line
clean_data = clear_lines(q_array)

res = split_questions(clean_data)
# print_by_lines(res)

dicts = to_dict(res)
# print_by_lines(dicts)

with(open('out.json', 'w', encoding='utf-8') as f):
    jsonString = json.dumps(dicts)
    content = f.write(jsonString)
