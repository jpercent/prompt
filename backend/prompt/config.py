import multiprocessing
bind = "127.0.0.1:8083"
workers = multiprocessing.cpu_count() * 2 + 1
debug = True
#propagate = False