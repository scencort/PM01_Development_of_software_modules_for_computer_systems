from service import BKPService

def main():
    bkp = BKPService()

    bkp.load_vkrs("vkrs.txt")

    bkp.save_languages_and_envs_json("languages_and_envs.json")
    bkp.save_most_popular_direction_json("most_popular_direction.json")

if __name__ == "__main__":
    main()