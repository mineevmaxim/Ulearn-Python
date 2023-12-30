import multiprocessing


def main():
    array_2d = input()[1: -1].split(', ')
    array_2d = [map(int, list(x[1: -1].split())) for x in array_2d]

    with multiprocessing.Pool(20) as pool:
        result = pool.map(worker_function, array_2d)

    print(sum(result))


if __name__ == "__main__":
    main()
