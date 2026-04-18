import os.path
import sys

from hit_object import HitObject
from parse_qua import get_qua_data
from hitobject_utils import merge_files_hitobjects, prevent_overlaps, order_hitobjects

def interface_get_user_input_data() -> tuple[str, str, list[list[HitObject]]]:
    base_metadata = ""
    files_hitobjects: list[list[HitObject]] = []

    print("Please provide an absolute filepath to the BASE chart (for timing and metadata) or type cancel to exit the program.")
    while True:
        base_path = input().strip()
        if os.path.isfile(base_path):
            base_metadata, *files_hitobjects = get_qua_data(base_path)
            break
        elif base_path.lower() == "cancel":
            print("Exiting program...")
            sys.exit(0)
        else:
            print(f"{base_path} was not recognized as a valid file. Please try again.")

    print("Now please provide absolute filepaths for every other chart to merge into the base chart.")
    print("Press enter after entering every filepath. Press enter on an empty line to start merging. Type cancel to exit the program.")
    while True:
        path = input().strip()
        hitobjects = []
        if os.path.isfile(path):
            _, hitobjects = get_qua_data(path)
            files_hitobjects.append(hitobjects)
        elif path == "":
            break
        elif path.lower() == "cancel":
            print("Exiting program...")
            sys.exit(0)
        else:
            print(f"{path} was not recognized as a valid file. Please try again.")
    
    return base_path, base_metadata, files_hitobjects



def main() -> None:
    base_filepath, base_metadata, files_hitobjects = interface_get_user_input_data()
    all_hitobjects = merge_files_hitobjects(files_hitobjects)
    all_hitobjects_no_overlaps = prevent_overlaps(all_hitobjects)
    all_hitobjects_no_overlaps_ordered = order_hitobjects(all_hitobjects_no_overlaps)
    stringified_hitobjects = list(map(str, all_hitobjects_no_overlaps_ordered))
    full_file_str = base_metadata + "".join(stringified_hitobjects)
    
    with open(base_filepath, "w") as original_qua_file:
        original_qua_file.write(full_file_str)
    print("Successfully merged all diffs.")



if __name__ == "__main__":
    main()