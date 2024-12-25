import datetime
import uuid
from typing import List

from fastapi import APIRouter, Path, Query, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from uvicorn.config import logger

from app.algorithm import w01_collect_ecmwf, w03_ready_to_use_ecmwf
from app.config.db_connection import get_db
from app.models.ecmwf_collect_hist import EcmwfCollectHist
from app.service import ecmwf_collect_hist_service

router = APIRouter()


@router.get("/w01")
async def collect_ecmwf(background_tasks: BackgroundTasks,
                        dates: List[str] = Query(),
                        db: Session = Depends(get_db)):

    transaction_id = str(uuid.uuid4()).replace("-", "")
    logger.info(f"====== transaction_id: {transaction_id} ======")
    now = datetime.datetime.now()
    collect_history = EcmwfCollectHist(
        transaction_id=transaction_id,
        request_dates=dates,
        status="started",
        created_at=now,
        updated_at=now
    )
    save_result = ecmwf_collect_hist_service.save_ecmwf_collect_history(db, collect_history)

    background_tasks.add_task(w01_collect_ecmwf.lists_by_dates, db, collect_history, dates)
    return save_result


@router.get("/w01/task-status/{transaction_id}")
def get_task_status(transaction_id: str = Path(...),
                    db: Session = Depends(get_db)):
    return w01_collect_ecmwf.get_task_status(db, transaction_id)


@router.get("/w03")
def ready_to_use_ecmwf(max_hr: int = Query(alias="max-hour"),
                       db: Session = Depends(get_db)):
    w03_ready_to_use_ecmwf.ready_to_use_ecmwf(db, max_hr)
    return {"max_hr": max_hr}
