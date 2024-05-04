# DNS Records Fetcher

## Overview
DNS Records Fetcher is a Python script designed to retrieve DNS records for a given domain. This tool supports fetching specific types of DNS records such as A, AAAA, MX, NS, TXT, CNAME, and SOA or all available records at once.

## Features
- **Fetch Specific Record Type:** Allows the user to specify a particular DNS record type to fetch, such as A, MX, etc.
- **Fetch All Records:** A convenient option to retrieve all supported types of DNS records for a domain with a single command.

## Requirements
- Python 3.x
- `dnspython` library

## Installation
To use this script, ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/). You will also need the `dnspython` library, which can be installed via pip. Here’s how to set up your environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Show help
To show command help and see available options, use the command:

```bash
python main.py -h
```

Fetch a Specific Type of DNS Record
To fetch a specific type of DNS record for a domain, use the following command:

```bash
python main.py example.com A
```


Here is how you might retrieve the MX records for example.com:

```bash
python main.py example.com MX
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
