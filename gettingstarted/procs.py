from hirefire.procs.rq import RQProc
from redis import StrictRedis
from urlparse import urlparse
import os
redistogo_url = 'redis://h:p1tpf6cgq7kagifamiktjuv006n@ec2-107-22-213-247.compute-1.amazonaws.com:24169'
u = urlparse(redistogo_url)


class WorkerProc(RQProc):
    name = 'worker'
    queues = ['high', 'default', 'low']
    connection = StrictRedis(host='ec2-107-22-213-247.compute-1.amazonaws.com', port='24169', db=0, password='p1tpf6cgq7kagifamiktjuv006n')