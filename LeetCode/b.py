R, C = len(grid), len(grid[0])

location = {}
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char not in '.#':
            location[char] = (i, j)


def neighbors(r, c):
    for rs, cs in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        r_, c_ = r + rs, c + cs
        if 0 <= r_ < R and 0 <= c_ < C:
            yield r_, c_


def bfs_from(source):
    r, c = location[source]
    seen = set([r, c])
    queue = collections.deque([(r, c, 0)])
    dist = {}

    while queue:
        r, c, d = queue.popleft()
        if source != grid[r][c] != '.':
            dist[grid[r][c]] = d
            continue
        for r_, c_ in neighbors(r, c):
            if grid[r_][c_] != '#' and (r_, c_) not in seen:
                queue.append((r_, c_, d + 1))
                seen.add((r_, c_))

    return dist


dists = {place: bfs_from(place) for place in location}
target_state = (1 << sum(ch.islower() for ch in location)) - 1
pq = [(0, '@', 0)]  # steps, position, status
final_dist = collections.defaultdict(lambda: inf)
final_dist['@', 0] = 0

while pq:
    d, place, state = heapq.heappop(pq)
    if final_dist[place, state] < d:
        continue  # exist better steps

    if state == target_state:
        return d

    for destination, d2 in dists[place].items():

        state2 = state
        if destination.islower():
            state2 |= (1 << (ord(destination) - ord('a')))
        elif destination.isupper():
            if not (state & (1 << (ord(destination) - ord('a')))):
                continue

        if d + d2 < final_dist[destination, state2]:
            final_dist[destination, state2] = d + d2
            heapq.heappush(pq, (d + d2, destination, state2))

return -1