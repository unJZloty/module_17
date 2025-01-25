from app.backend.db import engine, Base
from app.models.user import User
from app.models.task import Task
from sqlalchemy.schema import CreateTable

def main():
    # Создание таблиц в базе данных
    print("Создание таблиц в базе данных...")
    Base.metadata.create_all(bind=engine)

    # Вывод SQL-запросов для создания таблиц
    print("\nSQL для таблицы User:")
    print(CreateTable(User.__table__))

    print("\nSQL для таблицы Task:")
    print(CreateTable(Task.__table__))

if __name__ == "__main__":
    main()
