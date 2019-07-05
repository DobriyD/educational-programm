def main():
    n = int(input())
    a = map(int, input().split(maxsplit=n))
    print(*sorted(a))


if __name__ == "__main__":
    main()
