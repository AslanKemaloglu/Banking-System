# Banking System (CLI)

This project is a simple **command-line banking system** developed in Python.
It was created as a learning project to practice **core Python concepts** such as object-oriented programming, file handling, and basic security practices.

## Features

* Account creation and login system
* Password hashing using **SHA-256**
* Deposit and withdrawal operations
* Balance tracking
* Account activation and closure
* File-based data persistence
* Transaction logging with timestamps

## Technologies & Concepts Used

* Python 3
* Object-Oriented Programming (OOP)
* File I/O operations
* Password hashing (`hashlib`)
* Date and time handling (`datetime`)
* Basic input validation

## Project Structure

```
.
├── main.py
├── accounts.txt
├── transactions.txt
├── README.md
└── LICENSE
```

## How to Run

1. Clone the repository
2. Make sure Python 3.8 or higher is installed
3. Run the application:

```bash
python main.py
```

## Notes

* This project uses **text files** instead of a database for simplicity.
* No graphical interface or API is included.
* The focus is on core Python fundamentals rather than production-level architecture.

## Limitations

* No unit tests
* No database integration
* CLI-based interaction only

These limitations are intentional, as the project is meant to demonstrate foundational Python skills.

## License

This project is licensed under the MIT License.
