import datetime
import os
from datetime import datetime


class Logger:
    base_dir = "C:\\Users\\Alexander_Demin\\PycharmProjects\\pythonTestProject\\logs"
    log_date = datetime.now().strftime("%d.%m.%Y")
    log_dir = os.path.join(base_dir, log_date)
    log_time = datetime.now().strftime("%d.%m.%Y-%H.%M.%S")
    file_name = os.path.join(log_dir, f"log_{log_time}.log")
    os.makedirs(log_dir, exist_ok=True)

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"End time: {str(datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)
