class Applicant:
    def __init__(self, applicant_id, fio):
        self.applicant_id = int(applicant_id)
        self.fio = fio


    def __str__(self):
        return f"Applicant(applicant_id={self.applicant_id}, fio={self.fio})"


    def __repr__(self):
        return self.__str__()