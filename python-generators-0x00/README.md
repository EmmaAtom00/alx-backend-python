# Python Generators - 0x00

This project focuses on advanced Python generators to handle large datasets efficiently. It covers memory-efficient data processing, SQL database integration, and simulated real-world data streaming scenarios.

## Project Overview

In data-driven applications, memory management is key to performance. This project demonstrates how to use Python's `yield` keyword to create generators that stream data one row at a time, avoiding the high memory cost of loading massive datasets into RAM.

### Learning Objectives

- **Master Python Generators**: Create iterators that yield values on-the-fly.
- **Handle Large Datasets**: Use lazy loading to process extensive data without overloading memory.
- **Optimize Performance**: Minimize resource consumption for aggregate functions and streaming.
- **Apply SQL Knowledge**: Integrate Python with MySQL/MariaDB for dynamic data management.

## Files

| File | Description |
| --- | --- |
| `seed.py` | Implementation of database connection, initialization, and seeding. |
| `0-stream_users.py` | Generator that yields users from the database one by one. |
| `1-batch_processing.py` | Generator for fetching users in batches and processing them. |
| `user_data.csv` | Sample dataset used for seeding the `ALX_prodev` database. |
| `0-main.py` | Verification script for testing the seeding process. |
| `1-main.py` | Verification script for testing row streaming. |
| `2-main.py` | Verification script for testing batch processing. |
| `LEARNING.md` | Comprehensive deep-dive documentation into project concepts. |
| `README.md` | This file; project overview and instructions. |

## Requirements

- Python 3.x
- `mysql-connector-python`
- A running MySQL/MariaDB server

## Installation & Setup

1. **Install dependencies**:
   ```bash
   pip install mysql-connector-python
   ```

2. **Database Configuration**:
   The scripts use the following environment variables (defaults are provided in `seed.py`):
   - `ALX_MYSQL_HOST` (default: `localhost`)
   - `ALX_MYSQL_USER` (default: `root`)
   - `ALX_MYSQL_PWD` (default: empty string)

3. **Seeding the Database**:
   Run the main script to initialize the database and table, and seed it with data:
   ```bash
   python3 0-main.py
   ```

## Key Concepts

### Why Generators?
Regular functions load all results into memory before returning. Generators `yield` results one at a time, allowing you to process data that is larger than your available RAM.

### Lazy Loading
Data is only fetched from the source (file or database) when the program explicitly requests the next item. This is the cornerstone of building scalable, performant backend systems.
