class Employee:
    def __init__(self, name: str, emp_id: int):
        self._name = name
        self._id = emp_id

    def get_info(self) -> str:
        return f"Сотрудник: {self._name}, ID: {self._id}"
    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._id

class Manager:
    def __init__(self, department: str):
        self._department = department
    def manage_project(self) -> str:
        return f"Менеджер управляет проектами в отделе '{self._department}'."
    @property
    def department(self):
        return self._department

class Technician:
    def __init__(self, specialization: str):
        self._specialization = specialization
    def perform_maintenance(self) -> str:
        return f"Техник выполняет техническое обслуживание в области '{self._specialization}'."
    @property
    def specialization(self):
        return self._specialization
    
class TechManager(Employee, Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Employee.__init__(self, name, emp_id)
        Manager.__init__(self, department)
        Technician.__init__(self, specialization)
        self._team = []

    def add_employee(self, employee: Employee):
        if isinstance(employee, Employee):
            self._team.append(employee)
        else:
            raise TypeError("Можно добавлять только объекты класса Employee или его наследников! :) ")

    def get_team_info(self) -> str:
        if not self._team:
            return "В команде нет сотрудников."
        info = "Сотрудники в команде:\n"
        for emp in self._team:
            info += f"  - {emp.get_info()}\n"
        return info.strip()

    def get_info(self) -> str:
        return (f"TechManager: {self._name}, ID: {self._id}, "
                f"Отдел: {self._department}, Специализация: {self._specialization}")

if __name__ == "__main__":
    emp1 = Employee("Alex S", 3211)
    emp2 = Employee("Ivan I", 3212)

    # Менеджер
    manager = Manager("Маркетинг")
    print(manager.manage_project())

    # Техник
    tech = Technician("Сетевая инфраструктура")
    print(tech.perform_maintenance())

    tech_mgr = TechManager("Олег Тинькофф", 1, "IT", "Кибербезопасность")
    print(tech_mgr.get_info())
    print(tech_mgr.manage_project())
    print(tech_mgr.perform_maintenance())

    tech_mgr.add_employee(emp1)
    tech_mgr.add_employee(emp2)
    print(tech_mgr.get_team_info())
