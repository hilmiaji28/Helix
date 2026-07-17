"""
Prediction API Router.
"""

from fastapi import APIRouter, status

from api.constants import DEFAULT_RESPONSES
from api.logger import get_logger
from api.schemas import (
    PredictionRequest,
    PredictionResponse,
)
from api.services import prediction_service

logger = get_logger(__name__)


router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)


@router.post(
    "",
    summary="Predict customer purchase amount",
    description=(
        "Predict the customer's purchase amount using the "
        "trained CatBoost machine learning pipeline."
    ),
    operation_id="predictPurchaseAmount",
    response_model=PredictionResponse,
    status_code=status.HTTP_200_OK,
    responses={
        **DEFAULT_RESPONSES,
        200: {
            "description": "Prediction completed successfully.",
            "content": {
                "application/json": {"example": {"predicted_purchase_amount": 842.57}}
            },
        },
        422: {"description": "Input validation failed."},
        500: {"description": "Unexpected server error."},
    },
)
def predict(
    request: PredictionRequest,
) -> PredictionResponse:
    """
    Generate a purchase prediction from customer features.
    """

    logger.info("POST /predict request received.")

    result = prediction_service.predict(request.model_dump())

    logger.info("POST /predict completed successfully.")

    return PredictionResponse(**result)
