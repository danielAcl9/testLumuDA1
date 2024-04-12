# Lumu DNS Log Parser - Entry Test

## Description

The Lumu DNS Log Parser is a Python script designed to parse BIND Server logs and send the parsed DNS information to Lumu using the Collectors API. Lumu customers often require capturing DNS information from their internal DNS servers and sending it using our Collectors API. This script automates the process by parsing the log files and sending the data in chunks to Lumu's Custom Collector API.

## Features

- Parses BIND Server log files.
- Sends parsed DNS information to Lumu using the Collectors API.
- Data is sent in chunks of up to 500 records to optimize performance.
- Provides statistics after data transmission.
