from fastapi import APIRouter

router = APIRouter()


@router.post("")
def scan_label():
    raise NotImplementedError  # FR-300, FR-301, FR-302, FR-303
