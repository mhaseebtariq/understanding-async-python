# Understanding Python's Asynchronous Paradigm Using FastAPI Examples
We have set up 2 applications:
1. `api` - The api where we are defining `async` and `sync` http endpoints
2. `api-external` - The external api, that our `api` makes calls to 

## Setup
* **NOTE**: Run the code on an instance with at least 4 or more CPU cores
  * 1 for each api
  * 1 for the `test_executor.py`
* Setup and activate a Python 3.11+ environment
* `pip install "fastapi[standard]==0.115.12"`
* `pip install httpx==0.28.1`
* `cd api`
  * `fastapi run main.py --host 127.0.0.1 --port 8000 --workers 1`
* Open a new terminal
  * Activate the Python environment
  * `cd api-external`
  * `fastapi run main.py --host 127.0.0.1 --port 8001 --workers 1`
* Open a new terminal
  * Activate the Python environment
  * `python tests_executor.py "1,2,3,4,5,6,7,8,9,10,11"`

### Example Output
```
>> python tests_executor.py "1,2,3,4,5,6,7,8,9,10,11"

====================================================================================================
100 calls to `sync` in 16 seconds!
100 calls to `sync__external_sync` in 16 seconds!
10 calls to `async_without_async_code` in 30 seconds!
100 calls to `async_with_async_code_1` in 4 seconds!
50 calls to `async_with_async_code_1` + 50 calls to `async_with_async_code_2` in 4 seconds!
50 calls to `sync` in 10 seconds!
50 calls to `async_with_async_code_1` in 4 seconds!
50 calls to `sync` + 50 calls to `async_with_async_code_1` in 7 seconds!
50 calls to `sync__external_sync` + 50 calls to `async_with_async_code_1` in 7 seconds!
50 calls to `sync_cpu_bound` in 18 seconds!
50 calls to `sync_cpu_bound` + 50 calls to `async_with_async_code_1` in 24 seconds!
====================================================================================================
```
