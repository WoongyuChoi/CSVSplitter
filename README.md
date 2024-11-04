# CSVSplitter

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=fff&labelColor=grey&color=yellowgreen)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/WoongyuChoi/CSVSplitter/blob/main/LICENSE)
![Platform](https://img.shields.io/badge/platform-desktop-blue)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/WoongyuChoi/CSVSplitter)

<figure align="center">
    <img src="https://github.com/user-attachments/assets/4ac602f0-2503-4898-a337-c072372e65f6" width="80%"/>
</figure>

## Overview

**CSVSplitter** is a Python-based tool for splitting large CSV files into smaller, manageable chunks based on a specified number of rows. This utility is designed to handle large datasets efficiently, enabling users to break down files as needed.

## Features

- **Large CSV File Splitting**: Splits large CSV files into smaller files based on a specified number of rows.
- **Flexible Row Setting**: Customize the row count for each split file; the default setting is 10,000 rows.
- **Header Preservation**: All split files retain the original CSV file's header row.

## Setup

### Install Required Packages

CSVSplitter relies on the pandas library. Make sure to install the dependencies listed in the `equirements.txt` file:
```bash
pip install -r requirements.txt
```
## Usage

1. Run `csv_splitter.py` in the terminal or command prompt:
   ```bash
   python csv_splitter.py
   ```

2. Enter the name of the CSV file you want to split (without the file extension). For example, to split `sample.csv`, just type `sample`.

3. Specify the number of rows per split file. The default value is 10,000 rows. For example, enter `2000` if you want each file to contain up to 2,000 rows.

## Example

To split `sample.csv` into files of 1,000 rows each:
```bash
python csv_splitter.py
```

## License

This project is licensed under the MIT License.

