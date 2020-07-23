from init import init_map_files,init_data_collection
from CLI import run

def main():
    print("Louding system and prepering the system ...")
    map_files=init_map_files("python-data/.")
    map_substring=init_data_collection(map_files)
    print("The system is ready")
    run(map_substring,map_files)

if "__name__"==main:
    main()

main()