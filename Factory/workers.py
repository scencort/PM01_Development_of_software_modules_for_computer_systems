class Worker:
    def __init__(self, worker_id, name, brigade_id):
        self.worker_id = int(worker_id)
        self.name = name
        self.brigade_id = int(brigade_id)


    def __str__(self):
        return f"Worker(id={self.worker_id}, name={self.name}, brigade_id={self.brigade_id})"


    def __repr__(self):
        return self.__str__()   