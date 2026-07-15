from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
def register():
    raise NotImplementedError  # FR-001


@router.post("/login")
def login():
    raise NotImplementedError  # FR-002
