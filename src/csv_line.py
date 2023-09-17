from pydantic import BaseModel


class CsvLine(BaseModel):
    o2o1: float
    p8p7: float
    p4p3: float
    p7p3: float
    f4xFp2: float
    f3Fp1: float
    fp2fp1: float
    f8f7: float
    p8p4: float
    p4p3: float
    day: str
    notation: str
