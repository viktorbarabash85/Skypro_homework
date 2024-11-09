import logging
import os


def setup_logger(file_name: str, log_file: str) -> logging.Logger:
    """Функция настройки логирования для указанного файла."""

    # Создаем директорию для логов, если она не существует
    os.makedirs("logs", exist_ok=True)

    # Создаем логгер для данного файла
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)  # Уровень логирования не ниже DEBUG

    # Создаем обработчик для записи логов в файл
    full_log_file_path = f"logs/{log_file}.log"  # Добавляем .log к имени файла
    file_handler = logging.FileHandler(full_log_file_path, mode="w")  # Перезаписываем файл при каждом запуске
    file_handler.setLevel(logging.DEBUG)  # Уровень логирования для обработчика

    # Устанавливаем формат записи логов
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)
    return logger
