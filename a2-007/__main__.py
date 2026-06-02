def main():
    line = input().strip()
    if not line: return
    n, m = map(int, line.split())
    buckets = {}
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        buckets[i] = (a, b)
    targets = set(map(int, input().split()))
    children = {i: [] for i in range(1, n + 1)}
    roots = []
    for i in range(1, n + 1):
        parent = -1
        min_len = 999999999  # จำลอง
        ai, bi = buckets[i]
        for j in range(1, n + 1):
            if i == j: continue
            aj, bj = buckets[j]
            if aj < ai and bi < bj:
                length_j = bj - aj
                if length_j < min_len:
                    min_len = length_j
                    parent = j
        if parent == -1:
            roots.append(i)
        else:
            children[parent].append(i)

    def dfs(u):
        sum_buckets = 0
        child_nodes = []

        for v in children[u]:
            _c_count, _c_nodes = dfs(v)
            sum_buckets += _c_count
            child_nodes.extend(_c_nodes)

        if u in targets:
            return (1, [u])
        else:
            if sum_buckets == 0:
                return (0, [])
            elif sum_buckets == 1:
                return (1, child_nodes)
            else:
                return (1, [u])

    total_buckets = 0
    final_selection = []
    for r in roots:
        _c_count, _c_nodes = dfs(r)
        total_buckets += _c_count
        final_selection.extend(_c_nodes)
    final_selection.sort()
    print(total_buckets)
    print(" ".join(map(str, final_selection)))

main()