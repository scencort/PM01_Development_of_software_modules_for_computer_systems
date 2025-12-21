import json

from database_init import create_tables
from database import get_connection
from visitor import Visitor
from expert import Expert
from section import Section
from question import Question
from answer import Answer

class SpecialistService:
    def load_visitor(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                visitor_id, name = line.strip().split(";")

                visitor_id = int(visitor_id)

                cursor.execute(
                    "INSERT INTO visitor VALUES (?, ?)",
                    (visitor_id, name)
                )

        connection.commit()
        connection.close()


    def load_visitor_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT visitor_id, name FROM visitor"
        )

        zapros = cursor.fetchall()
        connection.close()

        visitor = []
        for z in zapros:
            visitor.append(
                Visitor(z[0], z[1])
            )

        return visitor


    def load_expert(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                expert_id, name = line.strip().split(";")

                expert_id = int(expert_id)

                cursor.execute(
                    "INSERT INTO expert VALUES (?, ?)",
                    (expert_id, name)
                )

        connection.commit()
        connection.close()


    def load_expert_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT expert_id, name FROM expert"
        )

        zapros = cursor.fetchall()
        connection.close()

        expert = []
        for e in zapros:
            expert.append(
                Expert(e[0], e[1])
            )

        return expert


    def load_section(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                section_id, name = line.strip().split(";")

                section_id = int(section_id)

                cursor.execute(
                    "INSERT INTO section VALUES (?, ?)",
                    (section_id, name)
                )

        connection.commit()
        connection.close()


    def load_section_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT section_id, name FROM section"
        )
        zapros = cursor.fetchall()
        connection.close()

        section = []
        for s in zapros:
            section.append(
                Section(s[0], s[1])
            )

        return section


    def load_question(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                question_id, visitor_id, section_id, date, is_closed = line.strip().split(";")

                question_id = int(question_id)
                visitor_id = int(visitor_id)
                section_id = int(section_id)
                is_closed = int(is_closed)

                cursor.execute(
                    "INSERT INTO question VALUES (?, ?, ?, ?, ?)",
                    (question_id, visitor_id, section_id, date, is_closed)
                )

        connection.commit()
        connection.close()


    def load_question_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT question_id, visitor_id, section_id, date, is_closed FROM question"
        )
        zapros = cursor.fetchall()
        connection.close()

        question = []
        for q in zapros:
            question.append(
                Question(q[0], q[1], q[2], q[3], q[4])
            )

        return question


    def load_answer(self, filename):
        connection = get_connection()
        cursor = connection.cursor()

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                answer_id, question_id, expert_id, date = line.strip().split(";")

                answer_id = int(answer_id)
                question_id = int(question_id)
                expert_id = int(expert_id)

                cursor.execute(
                    "INSERT INTO answer VALUES (?, ?, ?, ?)",
                    (answer_id, question_id, expert_id, date)
                )

        connection.commit()
        connection.close()


    def load_answer_from_db(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT answer_id, question_id, expert_id, date FROM answer"
        )
        zapros = cursor.fetchall()
        connection.close()

        answer = []
        for a in zapros:
            answer.append(
                Answer(a[0], a[1], a[2], a[3])
            )

        return answer

    """
    - кто из экспертов дал больше всех ответов за период с.. по..;
    """
    def most_answer_date(self, start_date, end_date):
        answers = self.load_answer_from_db()

        counts = {}

        for answer in answers:
            if start_date <= answer.date <= end_date:
                expert_id = answer.expert_id

                if expert_id not in counts:
                    counts[expert_id] = 0

                counts[expert_id] += 1

        print(counts)

        best_expert = None
        best_count = 0

        for expert_id, count in counts.items():
            if count > best_count:
                best_count = count
                best_expert = expert_id

        return {
            "best_expert": best_expert,
            "best_count": best_count
        }

    def save_most_answer_date_json(self, filename):
        most_answer_date = self.most_answer_date('2025-01-01', '2025-12-31')

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(most_answer_date, file, ensure_ascii=False, indent=4)

    """
    - число "незакрытых" вопросов без ответов по разделам на дату....
    """
    def not_closed_question(self, date):
        questions = self.load_question_from_db()
        answers = self.load_answer_from_db()

        answered_questions = set()

        for answer in answers:
            answered_questions.add(answer.question_id)

        resultat = {}

        for question in questions:
            if question.date <= date and question.is_closed == 0:
                if question.question_id not in answered_questions:
                    section_id = question.section_id

                    if section_id not in resultat:
                        resultat[section_id] = 0

                    resultat[section_id] += 1

        print(answered_questions)

        return resultat


    def save_not_closed_question_json(self, filename):
        not_closed_question = self.not_closed_question('2025-06-01')

        with open(filename, "w", encoding='utf-8') as file:
            json.dump(not_closed_question, file, ensure_ascii=False, indent=4)