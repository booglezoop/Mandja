from fastapi import APIRouter

router = APIRouter()


@router.post("")
def scan_barcode():
    raise NotImplementedError  # FR-200, FR-201, FR-202, FR-203
