import random
import concurrent.futures
import multiprocessing
import string
import time
import timeit


def getPriceData(data):
    data["increase"] = random.randint(-5, 5)
    random.randbytes(5)
    return data


myData: list = [
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"},
    {"token": random.randint(1000, 5000), "Symbol": "SBI-EQ"}
]
num_workers = 3
if __name__ == "__main__":
    start=time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        output = executor.map(getPriceData, myData)
    end=time.time()
    print(start-end)
    print(list(output))
