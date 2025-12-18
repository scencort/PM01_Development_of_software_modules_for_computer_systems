class Request:
    def __init__(self, request_id, equipment_id, object_id, request_date, is_installed, install_date):
        self.request_id = int(request_id)
        self.equipment_id = int(equipment_id)
        self.object_id = int(object_id)
        self.request_date = request_date
        self.is_installed = bool(is_installed)
        self.install_date = install_date


    def __str__(self):
        return f"Request(request_id={self.request_id}, equipment_id={self.equipment_id}, object_id={self.object_id}, request_date={self.request_date}, installed?={self.is_installed}, install_date={self.install_date}"


    def __repr__(self):
        return self.__str__()