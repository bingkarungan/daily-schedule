# Daily Schedule Maintainer

A simple command-line tool to manage your daily tasks and schedule. Built with Python, no external dependencies required.

## Features

- Add tasks with date and time
- View schedule by date
- Mark tasks as done
- Delete tasks
- Data saved locally in `schedule.json`

## Requirements

- Python 3.x

## How to Run

```bash
python3 schedule.py
```

## Usage

```
=== Daily Schedule Maintainer ===

1. View schedule
2. Add task
3. Mark task done
4. Delete task
5. Exit
```

- Date input defaults to **today** if left blank
- Tasks are automatically sorted by time
- Schedule data is stored in `schedule.json` in the same folder

## Example

```
--- Schedule for 2026-06-20 ---
1. [ ] 09:00 - Morning standup
2. [x] 10:00 - Review pull requests
3. [ ] 14:00 - Team meeting
```

## Contributing

1. Fork this repository
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'add: your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request
