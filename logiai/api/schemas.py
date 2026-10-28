"""Les fiches techniques (schémas Pydantic) de l'API LogiAI."""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Livraison(BaseModel):
    """Une livraison à évaluer : les 7 variables du contrat."""

    model_config = ConfigDict(extra="forbid")  # un champ inconnu est refusé (422)

    # Bornes PHYSIQUES : ce qu'un trajet réel peut afficher (pas le min/max du CSV).
    distance_km: float = Field(ge=1, le=1000, description="Distance du trajet (km)")
    poids_kg: float = Field(ge=0.1, le=20000, description="Poids transporté (kg)")
    heure_depart: int = Field(ge=0, le=23, description="Heure de départ (0 à 23)")
    pluie_mm: float = Field(ge=0, le=300, description="Pluie prévue sur le trajet (mm)")
    trafic_index: float = Field(ge=0, le=10, description="Trafic : 0 = fluide, 10 = saturé")
    nb_arrets: int = Field(ge=0, le=50, description="Nombre d'arrêts de livraison")
    type_vehicule: Literal["moto", "fourgon", "camion"] = Field(
        description="Type de véhicule : moto, fourgon ou camion"
    )


class PredictionOut(BaseModel):
    probabilite_retard: float = Field(ge=0, le=1, description="Probabilité que la livraison soit en retard")
    alerte: bool = Field(description="True si la probabilité atteint le seuil")
    seuil: float = Field(description="Seuil d'alerte utilisé")
    model_version: str = Field(description="Version du modèle")
