import json

from database import get_connection
from client import Client
from card import Card
from operation import Operation

class CardsService:
    def load_client(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                client_id, fio, passport, address = line.strip().split(";")

                client_id = int(client_id)
                passport = int(passport)

                cursor.execute(
                "INSERT INTO client VALUES (?, ?, ?, ?)",
                (client_id, fio, passport, address)
                )

        connection.commit()
        connection.close()


    def load_client_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT client_id, fio, passport, address FROM client"
        )

        zapros = cursor.fetchall()
        connection.close()

        client = []
        for c in zapros:
            client.append(
                Client(c[0], c[1], c[2], c[3])
            )

        return client


    def load_card(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                card_id, name, number, client_id, is_active = line.strip().split(";")

                card_id = int(card_id)
                number = int(number)
                client_id = int(client_id)
                is_active = int(is_active)

                cursor.execute(
                    "INSERT INTO card VALUES (?, ?, ?, ?, ?)",
                    (card_id, name, number, client_id, is_active)
                )

        connection.commit()
        connection.close()


    def load_card_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT card_id, name, number, client_id, is_active FROM card"
        )

        zapros = cursor.fetchall()
        connection.close()

        card = []
        for c in zapros:
            card.append(
                Card(c[0], c[1], c[2], c[3], c[4])
            )

        return card


    def load_operation(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                operation_id, card_id, date, type_operation = line.strip().split(";")

                operation_id = int(operation_id)
                card_id = int(card_id)

                cursor.execute(
                    "INSERT INTO operation VALUES (?, ?, ?, ?)",
                    (operation_id, card_id, date, type_operation)
                )

        connection.commit()
        connection.close()


    def load_operation_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT operation_id, card_id, date, type_operation FROM operation"
        )

        zapros = cursor.fetchall()
        connection.close()

        operation = []
        for o in zapros:
            operation.append(
                Operation(o[0], o[1], o[2], o[3])
            )

        return operation

    """
    - отпечатать список актуальных карт по примеру
    Название	Номер	Клиент
    Master Card	1	Антоненко Анна Васильевна
    Visa-electron	3	Петров Петр Петрович
    """
    def actual_card(self):
        cards = self.load_card_from_db()
        clients = self.load_client_from_db()

        client_id_fio = {}
        for client in clients:
            client_id_fio[client.client_id] = client.fio

        print(client_id_fio)

        resultat = []

        for card in cards:
            if card.is_active == 1:
                resultat.append({
                    "card_name": card.name,
                    "card_number": card.number,
                    "client": client_id_fio.get(card.client_id)
                })

        return resultat


    def save_actual_card_json(self, filename):
        actual_card = self.actual_card()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(actual_card, file, ensure_ascii=False, indent=4)


    """
    - распечатать журнал операций по примеру
    Дата проведения	ФИО	Номер	Название	Вид операции
    11.11.2008	Антоненко Анна Васильевна	1	Master Card	Открытие
    15.05.2009	Антоненко Анна Васильевна	1	Master Card	Пролонгирование
    """
    def journal(self):
        operations = self.load_operation_from_db()
        cards = self.load_card_from_db()
        clients = self.load_client_from_db()

        card_map = {}
        for card in cards:
            card_map[card.card_id] = card

        client_map = {}
        for client in clients:
            client_map[client.client_id] = client.fio

        resultat = []

        for operation in operations:
            card = card_map.get(operation.card_id)

            client_name = client_map.get(card.client_id)
            print("DEBUG client_name:", client_name)

            resultat.append({
                "date": operation.date,
                "client": client_name,
                "card_number": card.number,
                "card_name": card.name,
                "operation_type": operation.type_operation
            })

        return resultat


    def save_journal_json(self, filename):
        journal = self.journal()

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(journal, file, ensure_ascii=False, indent=4)