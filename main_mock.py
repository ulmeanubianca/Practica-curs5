from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class EfficiencyRequest(BaseModel):
    speed: int
    downtime: int
    quality_rate: float
    utilization_rate: float

def get_downtime():
    # Simulate an API call
    return 10

def calculate_efficiency(speed, quality_rate, utilization_rate):
    downtime = get_downtime()
    if not (0 <= quality_rate <= 1) or not (0 <= utilization_rate <= 1):
        raise ValueError("Quality rate and utilization rate must be between 0 and 1")
    if speed < 0 or downtime < 0:
        raise ValueError("Speed and downtime must be non-negative")

    downtime_hours = downtime / 60.0
    effective_production_time = (1 - downtime_hours) * utilization_rate
    efficiency = speed * effective_production_time * quality_rate

    return efficiency * 100

@app.post("/calculate_efficiency")
def calculate_efficiency_endpoint(request: EfficiencyRequest):
    try:
        efficiency = calculate_efficiency(
            request.speed,
            request.quality_rate,
            request.utilization_rate
        )
        return {"efficiency": efficiency}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
