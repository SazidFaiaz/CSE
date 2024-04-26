import sys
from collections import defaultdict
from math import gcd


def nearlySimilarRectangles(sides):
    ratio_count = defaultdict(int)

    for w, h in sides:
        # Reduce the ratio w:h to its simplest form
        g = gcd(w, h)
        ratio = (w // g, h // g)
        ratio_count[ratio] += 1

    similar_pairs = 0

    for count in ratio_count.values():
        if count > 1:
            similar_pairs += count * (count - 1) // 2

    return similar_pairs


if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])  # Read the number of rectangles
    sides = []

    for i in range(2, 2 * n + 2, 2):
        sides.append([int(data[i]), int(data[i + 1])])

    result = nearlySimilarRectangles(sides)
    print(result)
