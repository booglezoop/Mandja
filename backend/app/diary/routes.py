from fastapi import APIRouter

router = APIRouter()


@router.get("/{date}")
def get_diary(date: str):
    raise NotImplementedError  # FR-400, FR-404


@router.post("")
def create_entry():
    raise NotImplementedError  # FR-400


@router.patch("/{entry_id}")
def update_entry(entry_id: str):
    raise NotImplementedError  # FR-402


@router.delete("/{entry_id}")
def delete_entry(entry_id: str):
    raise NotImplementedError  # FR-403
