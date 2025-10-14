from dataclasses import dataclass
from typing import Optional

@dataclass
class Employe:
    id: int
    nom: str
    departement: str
    titre: str
    salaire_regulier: Optional[float]
    retro: Optional[float]
    autre: Optional[float]
    heures_sup: Optional[float]
    indemnisation_blessure: Optional[float]
    detail: Optional[float]
    prime_education: Optional[float]
    total_gains: Optional[float]
    code_postal: Optional[str]