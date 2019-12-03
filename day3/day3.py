import fileinput

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

class LineSegment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def intersect_with(self, line):
        x_range_a = set(range(self.start.x, self.end.x + 1))
        y_range_a = set(range(self.start.y, self.end.y + 1))

        x_range_b = set(range(line.start.x, line.end.x + 1))
        y_range_b = set(range(line.start.y, line.end.y + 1))

        x_intersection  = list(x_range_a & x_range_b)
        y_intersection  = list(y_range_a & y_range_b)

        if len(x_intersection) == 1 and len(y_intersection) == 1:
            return Point(x_intersection[0], y_intersection[0])
        else:
            return None
        

def parse_wire(wire_data):
    x = 0
    y = 0
    for movement in wire_data.split(","):
        direction = movement[0]
        offset = int(movement[1:])
        start = Point(x,y)

        if direction == "L":
            x = x - offset
        elif direction == "U":
            y = y + offset
        elif direction == "R":
            x = x + offset
        elif direction == "D":
            y = y - offset
        yield LineSegment(start,end=Point(x,y))

def get_wire_intersections(wireA, wireB):
    for segmentA in wireA:
        for segmentB in wireB:
            intersection = segmentA.intersect_with(segmentB)
            if intersection != None:
                yield intersection

input_data = fileinput.input()

first_wire = list(parse_wire(input_data.readline()))
second_wire = list(parse_wire(input_data.readline()))

center = Point(0, 0)
intersections = list(get_wire_intersections(first_wire, second_wire))
solution = sorted(intersections, key=lambda x: x.manhattan_distance(center))[0]

print(solution.manhattan_distance(center))
