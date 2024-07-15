from typing import List, Optional

from pydantic import BaseModel, conint, constr


class Stats(BaseModel):
    M: conint(ge=0, le=12)  # Movement
    WS: conint(ge=1, le=6)  # Weapon Skill
    BS: conint(ge=1, le=6)  # Ballistic Skill
    S: conint(ge=1, le=6)  # Strength
    T: conint(ge=1, le=6)  # Toughness
    W: conint(ge=1, le=3)  # Wounds
    I: conint(ge=1, le=6)  # Initiative
    A: conint(ge=1, le=3)  # Attacks
    Ld: conint(ge=1, le=10)  # Leadership
    Cl: conint(ge=1, le=10)  # Cool
    Wil: conint(ge=1, le=10)  # Willpower
    Int: conint(ge=1, le=10)  # Intelligence

class Equipment(BaseModel):
    name: str
    type: str
    cost: conint(ge=0)
    rarity: Optional[str]

class Skill(BaseModel):
    name: str
    level: conint(ge=1, le=5)

class Ganger(BaseModel):
    name: str
    stats: Stats
    equipment: List[Equipment]
    skills: List[Skill]
    status_effects: Optional[List[str]] = []

class Gang(BaseModel):
    name: str
    house: constr(regex=r'^(Escher|Goliath|Orlock|Van Saar|Cawdor|Delaque|Enforcers|Genestealer Cult|Chaos|Corpse Grinder Cult|Venator)$')
    reputation: conint(ge=0)
    wealth: conint(ge=0)
    gangers: List[Ganger]
    headquarters: Optional[str]
