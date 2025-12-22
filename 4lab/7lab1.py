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

class Manager(Employee):
    def __init__(self, name: str, emp_id: int, department: str):
        Employee.__init__(self, name, emp_id)
        self._department = department

    def manage_project(self) -> str:
        return f"Менеджер управляет проектами в отделе '{self._department}'."

    @property
    def department(self):
        return self._department

class Technician(Employee):
    def __init__(self, name: str, emp_id: int, specialization: str):
        Employee.__init__(self, name, emp_id)
        self._specialization = specialization

    def perform_maintenance(self) -> str:
        return f"Техник выполняет техническое обслуживание в области '{self._specialization}'."

    @property
    def specialization(self):
        return self._specialization

class TechManager(Manager, Technician):
    def __init__(self, name: str, emp_id: int, department: str, specialization: str):
        Technician.__init__(self, name, emp_id, specialization)
        Manager.__init__(self, name, emp_id, department)
        self._team = []

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("Можно добавлять только объекты класса Employee или его подклассов.")
        self._team.append(employee)

    def get_team_info(self) -> str:
        if not self._team:
            return "В команде нет сотрудников."
        return "Сотрудники в команде:\n" + "\n".join(f"  - {emp.get_info()}" for emp in self._team)

    def get_info(self) -> str:
        return (f"TechManager: {self._name}, ID: {self._id}, "
                f"Отдел: {self._department}, Специализация: {self._specialization}")

if __name__ == "__main__":
    emp1 = Employee("A N", 101)
    mgr = Manager("A C", 241, "Маркетинг")
    tech = Technician("A S", 331, "Сети")
    tech_mgr = TechManager("A M", 24, "IT", "Кибербезопасность")

    tech_mgr.add_employee(emp1)
    tech_mgr.add_employee(mgr)
    tech_mgr.add_employee(tech)

    print(tech_mgr.get_info())
    print(tech_mgr.manage_project())
    print(tech_mgr.perform_maintenance())
    print(tech_mgr.get_team_info())