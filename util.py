from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OptionScoreImgPath:
    score: int
    path: str | Path


def comboboxes_options(self):
    self.options_HMA = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 1": OptionScoreImgPath(2, "question.png"),
        "≥std 1": OptionScoreImgPath(3, "question.png"),
        "≥std 2A": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_HE = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 3": OptionScoreImgPath(2, "question.png"),
        "≥std 3 - <std 4": OptionScoreImgPath(3, "question.png"),
        "≥std 4": OptionScoreImgPath(4, "question.png"),
    }
    self.options_SE = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
    }
    self.options_IRMA = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Definite (all fields)": OptionScoreImgPath(3, "question.png"),
        "≥std 8A": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_VB = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Definite (2+ fields)": OptionScoreImgPath(3, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_NVD = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<std 10A": OptionScoreImgPath(2, "question.png"),
        "≥std 10A": OptionScoreImgPath(3, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_NVE = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "<1/2 Disc area": OptionScoreImgPath(2, "question.png"),
        "≥1/2 Disc area": OptionScoreImgPath(3, "question.png"),
    }
    self.options_FP = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "FPE only": OptionScoreImgPath(2, "question.png"),
        "FPD only": OptionScoreImgPath(3, "question.png"),
        "FPD + FPE": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_PRH_VH = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "PRH only": OptionScoreImgPath(2, "question.png"),
        "VH only": OptionScoreImgPath(3, "question.png"),
        "PRH+VH": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_EDEMA = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Present, not CSME": OptionScoreImgPath(2, "question.png"),
        "Present, CSME": OptionScoreImgPath(3, "question.png"),
        "Non-Diab": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    self.options_CTR = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Present, not CSME": OptionScoreImgPath(2, "question.png"),
        "Present, CSME": OptionScoreImgPath(3, "question.png"),
        "Non-Diab": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    self.options_VEN = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Definite": OptionScoreImgPath(2, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }

    self.options_LASER = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest/incomplete": OptionScoreImgPath(1, "question.png"),
        "Focal": OptionScoreImgPath(2, "question.png"),
        "Scatter only": OptionScoreImgPath(3, "question.png"),
        "Scatter + Focal": OptionScoreImgPath(4, "question.png"),
        "Could grade": OptionScoreImgPath(8, "question.png"),
    }
    self.options_RX = {
        "None": OptionScoreImgPath(0, "question.png"),
        "Quest": OptionScoreImgPath(1, "question.png"),
        "Focal RX only": OptionScoreImgPath(2, "question.png"),
        "Grid RX only": OptionScoreImgPath(3, "question.png"),
        "Focal + Grid": OptionScoreImgPath(4, "question.png"),
        "CG": OptionScoreImgPath(8, "question.png"),
    }
