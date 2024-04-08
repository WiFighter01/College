MOD = 10 ** 9 + 7


def dfs(v, parent, graph, dp):
    dp[v] = 1
    for u in graph[v]:
        if u == parent:
            continue
        dfs(u, v, graph, dp)
        dp[v] = (dp[v] * (dp[u] + 1)) % MOD


def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [0] * (n + 1)
    dfs(1, 0, graph, dp)

    total_paths = sum(dp) % MOD
    print(total_paths)


if __name__ == "__main__":
    main()
