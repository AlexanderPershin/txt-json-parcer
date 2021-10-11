from .is_part_of_q import is_part_of_q


def split_questions(content):
    prev_num = content[0]
    res_list = []
    curr_question = []
    for i in range(0, len(content)):
        item_num = content[i].split('.')[0]

        # print("=========================\n")
        # print("Prev_num:", prev_num, "\n")
        # print("Next_num:", item_num, "\n")

        if(is_part_of_q(prev_num, item_num)):
            curr_question.append(content[i])
        else:
            # print("Not in Question\n")
            res_list.append(curr_question)
            curr_question = []
            curr_question.append(content[i])
        prev_num = item_num

    return res_list
