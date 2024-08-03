from dataclasses import dataclass
from datetime import datetime
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
    
    img_pattern = re.compile(r"^(STDR\d+)_(\d{8})_(\d{6})_Color_([RL])_(\d{3})\.tif$")

    root_path = Path(root_dir)

    # 需要重写这个逻辑
    # Walk through the directory structure
    for file_path in root_path.rglob("*"):
        file_name = Path(file_path).name
        
        file_name_match = re.match(img_pattern,file_name)
        
        
        if file_name_match:=re.match(img_pattern, file_name):
            
            file_name = file_name_match.group(0)
            patient_id = file_name_match.group(1)
            date_string = file_name_match.group(2)
            visit_date = datetime.strptime(date_string, r"%Y%m%d").strftime(r"%Y-%m-%d")
            eye = file_name_match.group(4)
            
            patient_id_list.append(patient_id)
            visit_date_list.append(visit_date)
            eye_list.append(eye)
            file_path_list.append(file_path)
            

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
        "severity",
        # general
        "is_gradable",
        "clarity",
        "other_signs",
        "combobox_diagnoses",
        "other_diagnoses",
        "ICDR",
        # etdr
        "MA",
        "RH",
        "RH_quadrants",
        "HE",
        "CSME",
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
