# Recipe 2.12 Using **kwargs to accept arbitrary keyword arguments in a function
def connect(**kwargs):
    """Print the received keyword arguments and simulate a connection."""
    print("kwargs:", kwargs)
    host = kwargs.get("host", "localhost")
    port = kwargs.get("port", 80)
    secure = kwargs.get("secure", False)
    print(f"Connecting to {host}:{port} (secure={secure})")
    return {"host": host, "port": port, "secure": secure}

if __name__ == "__main__":
   
    # simple call as in the example
    connect(host="localhost", port=8080)

    # extra options
    connect(host="example.com", port=443, secure=True, timeout=10)

    # unpack a dict of parameters
    params = {"host": "api.service", "port": 5000}
    connect(**params)