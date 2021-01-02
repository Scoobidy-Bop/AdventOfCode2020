import io
import os
import sys


def main():
    ret = 0
    if len(sys.argv) > 1:
        ret = solve("test.txt")
        print("Expected Pt1 answer: 514579")
        print("Pt1 Answer is: " + str(ret))

        ret = solve2("test.txt")
        print("Expected Pt2 answer: 241861950")
        print("Pt2 Answer is: " + str(ret))

    else:
        ret = solve("input.txt")
        print("Pt1 Answer is: " + str(ret))

        ret = solve2("input.txt")
        print("Pt2 Answer is: " + str(ret))


def solve(f_name):
    location = os.path.abspath(f_name)
    content = []
    with open(location) as f:
        for line in f:
            content.append(int(line.strip("\n")))

    val = 2020
    half = val / 2
    good = {val - x for x in content if x <= half} & {x for x in content if x > half}
    pairs = {(val - x, x) for x in good}
    ints = pairs.pop()
    ans = ints[0] * ints[1]

    return ans


def solve2(f_name):
    location = os.path.abspath(f_name)
    content = []
    with open(location) as f:
        for line in f:
            content.append(int(line.strip("\n")))

    val = 2020
    ans = 1
    content.sort()
    for i in range(0, len(content) - 2):
        l = i + 1
        r = len(content) - 1
        while l < r:
            if content[i] + content[l] + content[r] == val:
                print("Vals: {}, {}, {}".format(content[i], content[l], content[r]))
                ans = content[i] * content[l] * content[r]
                break
            elif content[i] + content[l] + content[r] > val:
                r -= 1
            else:
                l += 1

    return ans


if __name__ == "__main__":
    main()