from service import SpecialistService
from database_init import create_tables

def main():
    ss = SpecialistService()

    create_tables()

    ss.load_visitor("visitor.txt")
    ss.load_expert("expert.txt")
    ss.load_section("section.txt")
    ss.load_question("question.txt")
    ss.load_answer("answer.txt")

    ss.save_most_answer_date_json("most_answer_date_json.json")

    ss.save_not_closed_question_json("not_closed_question_json.json")

if __name__ == "__main__":
    main()