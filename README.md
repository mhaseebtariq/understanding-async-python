# Understanding Python Asynchronous Paradigm Using FastAPI Examples
We have set up 2 applications:
1. `api` - The api where we are defining `async` and `sync` http endpoints
2. `api-external` - The external api, that our `api` makes calls to 

## Setup
* NOTE: Run the code on an instance with at least 4 or more CPU cores
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
