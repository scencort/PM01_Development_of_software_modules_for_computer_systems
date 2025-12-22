class Application:
    def __init__(self, application_id, applicant_id, type_document_id, date):
        self.application_id = int(application_id)
        self.applicant_id = int(applicant_id)
        self.type_document_id = int(type_document_id)
        self.date = date


    def __str__(self):
        return f"Application(application_id={self.application_id}, applicant_id={self.applicant_id}, type={self.type_document_id}, date={self.date}"


    def __repr__(self):
        return self.__str__()