# Firewall README

## Overview

This Python program implements a basic firewall using socket programming. The firewall listens for incoming TCP connections and applies filtering rules based on the source IP address and port number of each connection attempt. It demonstrates how to control network access based on predefined criteria, allowing or blocking connections accordingly.

## Features

- **Socket Communication**: Uses `socket` module to create a TCP socket for handling incoming connections.
- **Packet Filtering**: Implements simple filtering logic to allow connections only from specified IP addresses and ports.
- **Logging**: Outputs connection events and filtering decisions to standard output for monitoring and debugging purposes.

## Requirements

- Python 3.x
- Standard Python `socket` module (no additional libraries required)

## Usage

### Installation

1. Ensure Python 3.x is installed on your system.
2. Download or clone the repository containing the firewall script.

### Configuration

- **Rule Definition**: Modify the `is_allowed` method in the `Firewall` class to define specific IP addresses (`allowed_ips`) and ports (`allowed_ports`) that are allowed to connect. By default, it allows connections only from `127.0.0.1` on port `8080`.

### Running the Firewall

1. Open a terminal or command prompt.
2. Navigate to the directory containing the firewall script.
3. Run the firewall script using Python:

   ```bash
   python firewall.py

4. The firewall will start listening for incoming connections on 0.0.0.0:12345 by default. You can modify these settings in the Firewall class initialization (__init__ method).
   ```bash
   if __name__ == "__main__":
    firewall = Firewall()
    firewall.start()
- This snippet initializes and starts the firewall with default settings (host='0.0.0.0', port=12345).
