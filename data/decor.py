def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print(f"Время выполнения функции {func.__name__} = {end - start}")
    
    return wrapper

