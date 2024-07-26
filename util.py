from dataclasses import dataclass
from pathlib import Path
import re
import pandas as pd
from pathlib import Path

DATA_BASE_PATH = Path.home() / "ETDR-grading-app"
DF_DATABASE_PATH = DATA_BASE_PATH / "df_database.parquet"
DF_GRADED_PATH = DATA_BASE_PATH / "df_graded.parquet"


@dataclass(frozen=True)
class OptionScoreImgPath:
    score: int
    path: str | Path


def get_df_folder_contents(root_dir):
    patient_id_list = []
    visit_date_list = []
    file_path_list = []
    eye_list = []

    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    eye_pattern = re.compile(r"_Color_(L|R)_")

    root_path = Path(root_dir)

    # Walk through the directory structure
    for file_path in root_path.rglob("*"):
        if file_path.is_file():
            # Get the parent directories
            parents = list(file_path.parents)
            if len(parents) >= 2:  # Ensure there are at least 2 parts for dir1 and dir2
                dir1 = parents[1].name
                dir2 = parents[0].name
                if date_pattern.match(dir2):  # Check if dir2 matches the date pattern
                    patient_id_list.append(dir1)
                    visit_date_list.append(dir2)
                    file_path_list.append(str(file_path))

                    # Extract 'L' or 'R' from the filename
                    match = eye_pattern.search(file_path.name)
                    if match:
                        eye_list.append(match.group(1))
                    else:
                        eye_list.append(None)

    # Create a DataFrame from the lists
    df = pd.DataFrame(
        {
            "patient_id": patient_id_list,
            "visit_date": visit_date_list,
            "file_path": file_path_list,
            "eye": eye_list,
        }
    )

    return df


def load_or_create_df_database(filename=DF_DATABASE_PATH):
    columns = [
        # basic info
        "patient_id",
        "visit_date",
        "grader",
        "eye",
        "levels",
        "FP_type",
        # general
        "is_gradable",
        "clarity",
        "is_dr",
        "combobox_diagnoses",
        "other_diagnoses",
        "ICDR",
        # etdr
        "MA",
        "RH",
        "RH_quadrants",
        "HE",
        "SE",
        "IRMA",
        "IRMA_quadrants",
        "VB",
        "VB_quadrants",
        "NVD",
        "NVE",
        "NVE_quadrants",
        "FP",
        "PRH_VH",
        "VEN",
        "LASER",
        "RD"
        # others
        "confident",
        "comment",
    ]

    file_path = Path(filename)

    if file_path.exists():
        df = pd.read_parquet(file_path)
    else:
        df = pd.DataFrame(columns=columns)
    return df


def load_or_create_df_graded(filename=DF_GRADED_PATH):
    columns = [
        "patient_id",
        "visit_date",
        "eye",
    ]

    file_path = Path(filename)

    if file_path.exists():
        df = pd.read_parquet(file_path)
    else:
        df = pd.DataFrame(columns=columns)
    return df
