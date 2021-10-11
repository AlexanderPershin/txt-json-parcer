from .conv_int import conv_int


def is_part_of_q(prev, next):
    # Check if two id next to each other are part of the same question
    prev_converted = conv_int(prev)
    next_converted = conv_int(next)
    if(prev_converted[0] and next_converted[0]):
        # both numbers
        num1 = prev_converted[0]
        num2 = next_converted[0]
        num1_val = prev_converted[1]
        num2_val = next_converted[1]
        diff = num1_val - num2_val
        # print('Diff prev - next:', diff)
        if(num1_val == 1 and num2_val == 1):
            # First q
            return True
        elif(num1_val == num2_val):
            return False
        elif(diff == -1):
            return True
        elif(num1_val == 5 and num2_val < num1_val):
            return False
        elif(diff > 1):
            return True
    elif(prev_converted[0] and not next_converted[0]):
        # Question header and a)Answer
        return True
    elif(not prev_converted[0] and not next_converted[0]):
        # Both letters
        return True
    else:
        return False
