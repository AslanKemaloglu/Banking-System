# Banking System (CLI)

This project is a simple **command-line banking system** developed in Python.
User data files are created **automatically at runtime** when the application is executed.

## Features

* Account creation and login system
* Password hashing using **SHA-256**
* Deposit and withdrawal operations
* Balance tracking
* Account activation and closure
* File-based persistence
* Transaction logging with timestamps

## Technologies & Concepts Used

* Python 3
* Object-Oriented Programming (OOP)
* File I/O operations
* Password hashing (`hashlib`)
* Date and time handling (`datetime`)
* Decimal usage for monetary values
* Basic input validation

## Concepts Demonstrated

* Object-oriented design with multiple classes
* Secure handling of user passwords
* Monetary calculations handled safely
* Simple persistence using text files instead of a database

## Project Structure

```
.
├── main.py
├── README.md
└── LICENSE
```

> Note:
> `accounts.txt` and `transactions.txt` are **not included** in the repository.
> These files are created automatically when the program runs.

## How to Run

1. Clone the repository
2. Make sure Python 3.8 or higher is installed
3. Run the application:

```bash
python main.py
```

Then follow the menu options in the terminal.

## Limitations

* No unit tests
* No database integration
* CLI-based interaction only

These limitations are intentional, as the project focuses on demonstrating **core Python fundamentals** rather than production-level architecture.

## License

This project is licensed under the MIT License.
