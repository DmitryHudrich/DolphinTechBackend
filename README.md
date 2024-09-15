# how to run
- `python venv venv` in repo for venv
- `poetry install` for install dependencies
- import following env vars:
    - `IUBIP_GROUPS_URL=https://www.iubip.ru/local/templates/univer/include/schedule/ajax/read-file-groups.php`
    - `MOBILE_SCHEDULE_RKSI_URL=https://www.rksi.ru/mobile_schedule`
    - `SCHEDULE_RKSI_URL=https://www.rksi.ru/schedule`
    - `RGUPS_URL=https://www.rgups.ru/services/time/`
- run python:
    - `python main.py`

# an easer way:
- ```
    python -m venv venv && source ./venv/bin/activate && poetry install && echo "
    IUBIP_GROUPS_URL=https://www.iubip.ru/local/templates/univer/include/schedule/ajax/read-file-groups.php
    MOBILE_SCHEDULE_RKSI_URL=https://www.rksi.ru/mobile_schedule
    SCHEDULE_RKSI_URL=https://www.rksi.ru/schedule
    RGUPS_URL=https://www.rgups.ru/services/time/
    " >> .env
    ```
- ```
    export $(grep -v '^#' .env | xargs -d '\n') python main.py
    ```
