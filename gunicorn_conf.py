# workers = 5    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
# worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
# bind = "0.0.0.0:8888"    # 监听IP放宽，以便于Docker之间、Docker和宿主机之间的通信


# -*- coding: utf-8 -*-

from multiprocessing import cpu_count

bind = ["127.0.0.1:9000"]
daemon = False  # 是否开启守护进程模式
pidfile = 'gunicorn.pid'

workers = cpu_count() * 2
worker_class = "gevent"
worker_connections = 65535

keepalive = 60
timeout = 30
graceful_timeout = 10
forwarded_allow_ips = '*'

# # # 日志处理
# # capture_output = True
# # loglevel = 'info'
# # errorlog = 'error.log'
