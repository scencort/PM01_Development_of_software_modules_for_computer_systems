from service import FactoryService

def main():
    fs = FactoryService()

    fs.load_brigades("brigades.txt")
    fs.load_workers("workers.txt")
    fs.load_parts("parts.txt")
    fs.load_productions("products.txt")

    fs.save_no_defect_brigades_json("no_defect_brigades_json.json")

if __name__ == "__main__":
    main()