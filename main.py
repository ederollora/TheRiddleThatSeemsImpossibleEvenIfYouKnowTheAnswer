# Explanation of the problem
# https://www.youtube.com/watch?v=iSNsgj1OCLA

import sys
import random

def calculate_loops(my_boxes):
    loops = []
    current_loop = []

    box_number = 0

    while True:

        if box_number is None:
            break

        next_box = my_boxes[box_number]

        current_loop.append((box_number, next_box))

        # Position is done
        my_boxes[box_number] = 0

        if next_box == current_loop[0][0]:
            loops.append(current_loop)
            current_loop = []
            # We get the first non zero number in the list. 0-ed list positions have already been picked.
            box_number = first_non_zero(my_boxes)
        else:
            box_number = next_box

    # print_loop_contents(loops)

    for loop in loops:
        if len(loop) > int(len(my_boxes) / 2):
            return False

    return True


def print_loop_contents(loops):
    print("Number of loops {}.".format(len(loops)))
    for i, loop in enumerate(loops):
        print("Loop {}, Length: {}: ".format(i + 1, len(loop)), end="")
        for j, box in enumerate(loop):
            print("{}[{}]".format(box[0] + 1, box[1] + 1), end="")
            if j + 1 != len(loop):
                print(" -> ", end="")
        print("")


# https://stackoverflow.com/a/64466108
def first_non_zero(boxes_to_check):
    try:
        return next(idx for idx, value in enumerate(boxes_to_check) if value != 0)
    except StopIteration:
        return None


def main():

    MAX_PRISONERS = 100
    MAX_TESTS = 100000

    if len(sys.argv) > 1:
        MAX_TESTS = int(sys.argv[1])

    prisoner_numbers = list(range(0, MAX_PRISONERS))

    results = []
    for t in range(MAX_TESTS):
        boxes = prisoner_numbers.copy()
        random.shuffle(boxes)
        results.append(calculate_loops(boxes))
        # if t % 10000 == 0:
        #    print("Test {}.".format(t))

    total_true = sum(results)
    print("Favorable cases: {}".format((total_true / len(results)) * 100))


if __name__ == "__main__":
    main()
