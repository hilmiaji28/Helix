from datetime import date

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    Age: int = Field(..., ge=10, le=100)

    Gender: str

    City: str

    Product_Category: str

    Payment_Method: str

    Device_Type: str

    Session_Duration_Minutes: float = Field(..., gt=0)

    Pages_Viewed: int = Field(..., gt=0)

    Is_Returning_Customer: int = Field(..., ge=0, le=1)

    Delivery_Time_Days: int = Field(..., ge=0)

    Customer_Rating: float = Field(..., ge=1, le=5)

    Transaction_Date: date


class PredictionResponse(BaseModel):
    predicted_purchase_amount: float
