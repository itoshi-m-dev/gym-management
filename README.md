# 🏋️ Gym Management System

This project is a simple simulation of a gym management system built with Python. The idea is to allow the registration of students, instructors, and exercises, while automatically logging all activities.

## 📂 What's in the project?

- `main.py` – Contains all the logic of the system (classes and basic test).
- `log_academia.txt` – File where notifications are stored.

## ✅ What can you do with it?

- Register students, instructors, and exercises.
- Assign students to instructors.
- Add training routines for students.
- Automatically generate a log of all actions in the system.

## 🧱 How does it work?

The system uses the following main classes:

- `Pessoa` (Person): Base class for students and instructors.
- `Aluno` (Student): Can have a list of training exercises.
- `Instrutor` (Instructor): Can manage a group of students.
- `Exercicio` (Exercise): Represents a workout with a name, muscle group, and duration.
- `Academia` (Gym): Manages the whole system — students, instructors, exercises, and notifications.
- `NotificaçãoMixin`: A mixin that logs notifications to a text file.

## 🧪 Example usage

```python
joao = Aluno('Joao', 20, 1)
ava = Instrutor('Ava Max', 30, 2, 'Musculação')
ex1 = Exercicio('Cadeira Extensora', 'Pernas', 30)
acad = Academia('Panobianco')

acad.cadastrar_alunos(joao.nome)
acad.cadastrar_instrutor(ava.nome)
acad.cadastrar_exercicio(ex1.nome)
```

Notifications are automatically written to `log_academia.txt`.

## 💡 Possible improvements

- Add `__str__` methods to classes to make log entries more readable.
- Improve how objects are passed in notifications to avoid memory address logs.
- Build a graphical interface or web API for better usability.
- Replace flat file logging with database storage.

---

### 👨‍💻 Created by Emanuel Pinheiro de Freitas Mellina

---
