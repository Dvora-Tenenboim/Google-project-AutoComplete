from init import init_map_files, init_data_collection
from CLI import run

PATH = "python-data/."


def main():
    print("Loading system and preparing the system ...")
    map_files = init_map_files(PATH)
    map_substring = init_data_collection(map_files)
    print("The system is ready")
    run(map_substring, map_files)


if __name__ == "__main__":
    main()
