from fastapi import APIRouter, status

router = APIRouter(
    responses={status.HTTP_404_NOT_FOUND: {"detail": "Not found"}},
)


@router.get("/healthy", status_code=status.HTTP_200_OK)
def liveness():
    return "Healthy as a fish"


@router.get("/ready", status_code=status.HTTP_200_OK)
def readiness():
    return "Ready as an egg"
