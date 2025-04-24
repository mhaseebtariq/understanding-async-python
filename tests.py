import re
import sys
import threading
import time
import urllib.request
import uuid

API = "http://127.0.0.1:8000/api"


def call_api(url):
    return urllib.request.urlopen(url).read()


def construct_urls(endpoint, times):
    return [f"{API}/{endpoint}?rid={uuid.uuid4()}" for _ in range(times)]


def execute_multithreaded_api_calls(urls):
    threads = [threading.Thread(target=call_api, args=(url,)) for url in urls]
    for thread in threads:
        thread.start()
    start = time.time()
    for thread in threads:
        thread.join()
    return round(time.time() - start)


def test_1():
    urls = construct_urls("sync", 100)
    return f"100 calls to `sync` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_2():
    urls = construct_urls("sync__external_sync", 100)
    return f"100 calls to `sync__external_sync` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_3():
    urls = construct_urls("async_without_async_code", 10)
    return f"10 calls to `async_without_async_code` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_4():
    urls = construct_urls("async_with_async_code_1", 100)
    return f"100 calls to `async_with_async_code_1` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_5():
    urls = construct_urls("async_with_async_code_1", 50)
    urls += construct_urls("async_with_async_code_2", 50)
    return (
        "50 calls to `async_with_async_code_1` "
        f"+ 50 calls to `async_with_async_code_2` in {execute_multithreaded_api_calls(urls)} seconds!"
    )


def test_6():
    urls = construct_urls("sync", 50)
    return f"50 calls to `sync` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_7():
    urls = construct_urls("async_with_async_code_1", 50)
    return f"50 calls to `async_with_async_code_1` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_8():
    urls = construct_urls("sync", 50)
    urls += construct_urls("async_with_async_code_1", 50)
    return (
        "50 calls to `sync` "
        f"+ 50 calls to `async_with_async_code_1` in {execute_multithreaded_api_calls(urls)} seconds!"
    )


def test_9():
    urls = construct_urls("sync__external_sync", 50)
    urls += construct_urls("async_with_async_code_1", 50)
    return (
        "50 calls to `sync__external_sync` "
        f"+ 50 calls to `async_with_async_code_1` in {execute_multithreaded_api_calls(urls)} seconds!"
    )


def test_10():
    urls = construct_urls("sync_cpu_bound", 50)
    return f"50 calls to `sync_cpu_bound` in {execute_multithreaded_api_calls(urls)} seconds!"


def test_11():
    urls = construct_urls("sync_cpu_bound", 50)
    urls += construct_urls("async_with_async_code_1", 50)
    return (
        "50 calls to `sync_cpu_bound` "
        f"+ 50 calls to `async_with_async_code_1` in {execute_multithreaded_api_calls(urls)} seconds!"
    )


if __name__ == "__main__":
    tests = {k: v for k, v in locals().items() if re.match("^test_[\d+]", k)}
    if len(sys.argv) < 2:
        raise Exception("Please provide an argument for the test number")
    test_number = int(sys.argv[1].strip())
    print(tests[f"test_{test_number}"]())
