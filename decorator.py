import time


def time_it(sample):
    print("time_it")

    def wrapper():
        print("wrapper")
        start = time.time()
        res = sample()
        end = time.time()
        print("Took: " + str((start-end)*1000))
        return res
    return wrapper


@time_it  # or sample = time_it(sample)
def sample():
    print("Sample")
    a = list(map(lambda x: x*2, [1, 2, 3]))
    time.sleep(1)
    return a
sample()