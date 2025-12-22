class Product:
    def __init__(self, date, worker_id, brigade_id, part_id, is_defect):
        self.date = date
        self.worker_id = int(worker_id)
        self.brigade_id = int(brigade_id)
        self.part_id = int(part_id)
        self.is_defect = int(is_defect)


    def __str__(self):
        return f"Product(worker_id={self.worker_id}, brigade_id={self.brigade_id}, part_id={self.part_id}, defect?={self.is_defect}, date={self.date}"


    def __repr__(self):
        return self.__str__()