from typing import List

def sort_squares(nums):
    pos_sqs = []
    neg_sqs = []
    for n in nums:
        if n < 0:
            neg_sqs.append(n*n)
        else:
            pos_sqs.append(n*n)
    sorted_sqs = []
    i = 0
    j = len(neg_sqs) - 1
    while (i < len(pos_sqs)) and (j > -1):
        if pos_sqs[i] < neg_sqs[j]:
            sorted_sqs.append(pos_sqs[i])
            i += 1
        else:
            sorted_sqs.append(neg_sqs[j])
            j -= 1
    while i < len(pos_sqs):
        sorted_sqs.append(pos_sqs[i])
        i += 1
    while j >= 0:
        sorted_sqs.append(neg_sqs[j])
        j -= 1
    return sorted_sqs