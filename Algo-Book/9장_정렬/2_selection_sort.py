# def selection_sort(seq):
#     for i in range(len(seq) - 1, 0, -1):
#         max_j = i
#         for j in range(max_j):
#             if seq[j] > seq[max_j]:
#                 max_j = j
#                 seq[i], seq[max_j] = seq[max_j], seq[i]
#     return seq


def selection_sort(seq):
    length = len(seq)
    for i in range(length-1):
        min_j = i
        for j in range(i+1, length):
            if seq[min_j] > seq[j]:
                min_j = j
        seq[i], seq[min_j] = seq[min_j], seq[i]
        print(seq)
    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert(selection_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_selection_sort()
