import json
from datetime import datetime, timedelta
from database import get_connection

class Mfc:
    def load_document_type(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                type_id, name = line.strip().split(";")

                type_id = int(type_id)

                cursor.execute(
                    "INSERT INTO type_document VALUES (?, ?)",
                    (type_id, name)
                )

        connection.commit()
        connection.close()


    def load_applicant(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                applicant_id, fio = line.strip().split(";")

                applicant_id = int(applicant_id)

                cursor.execute(
                    "INSERT INTO applicant VALUES (?, ?)",
                    (applicant_id, fio)
                )

        connection.commit()
        connection.close()


    def load_application(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                application_id, applicant_id, type_document_id, date = line.strip().split(";")

                application_id = int(application_id)
                applicant_id = int(applicant_id)
                type_document_id = int(type_document_id)

                cursor.execute(
                    "INSERT INTO application VALUES (?, ?, ?, ?)",
                    (application_id, applicant_id, type_document_id, date)
                )

        connection.commit()
        connection.close()

    """
    - отпечатать список типов документов в порядке убывания количества поданных заявок за период;
    """
    def type_document_count(self, start_date, end_date):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT type_document_id, date FROM application "
        )

        zapros = cursor.fetchall()
        connection.close()


        kol_vo = {}
        for type_document_id, date in zapros:
            if start_date <= date <= end_date:
                if type_document_id not in kol_vo:
                    kol_vo[type_document_id] = 0
                kol_vo[type_document_id] += 1


        resultat = sorted(
            kol_vo.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return resultat


    def save_document_type_json(self, filename, start_date, end_date):
        type_document = self.type_document_count(start_date, end_date)

        resultat = []
        for type_document_id, count in type_document:
            resultat.append({
                "document_type_id": type_document_id,
                "count": count
            })

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(resultat, file, ensure_ascii=False, indent=4)


    """
    - определить, когда заявитель N может получить социальную карту.
    """
    def get_social_card(self, applicant_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT date FROM application "
            "WHERE applicant_id = ? AND type_document_id = 1 ",
            [applicant_id]
        )

        zapros = cursor.fetchall()
        connection.close()


        if not zapros:
            return None

        date_str = zapros[0][0]
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")


        ready_date = date_obj + timedelta(days=45)

        return ready_date.strftime("%Y-%m-%d")


    def save_get_social_card_json(self, applicant_id, filename):
        date = self.get_social_card(applicant_id)

        resultat = {
            "applicant_id": applicant_id,
            "social_card_ready_date": date
        }

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(resultat, file, ensure_ascii=False, indent=4)