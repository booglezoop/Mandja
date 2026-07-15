from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_foods():
    raise NotImplementedError  # FR-103


@router.post("")
def create_food():
    raise NotImplementedError  # FR-100


@router.patch("/{food_id}")
def update_food(food_id: str):
    raise NotImplementedError  # FR-101


@router.delete("/{food_id}")
def delete_food(food_id: str):
    raise NotImplementedError  # FR-102
