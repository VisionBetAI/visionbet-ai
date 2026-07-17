from pydantic import BaseModel


class Match(BaseModel):
    home_team: str
    away_team: str

    home_goals_avg: float = 0.0
    away_goals_avg: float = 0.0

    home_corners_avg: float = 0.0
    away_corners_avg: float = 0.0