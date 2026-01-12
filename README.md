[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)



![Logo](https://github.com/thelonewolf39/homebrew-CrossCast/blob/main/images/logo.png?raw=true)


![GitHub License](https://img.shields.io/github/license/thelonewolf39/homebrew-CrossCast)

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://stand-with-ukraine.pp.ua)



[![Contributors](https://contrib.rocks/image?repo=thelonewolf39/homebrew-CrossCast)](https://github.com/theonewolf39/homebrew-CrossCast/graphs/contributors)

# CrossCast

CrossCast is a simple cross-platform CLI tool for sending files between Windows, Mac, and Linux systems, similar to AirDrop.

## Features
- Send files from Windows to Mac/Linux and vice versa
- Discover receivers on your local network (`find` command)
- Easy local testing
- Fun easter egg command
- Solidarity with Ukraine ([#WeSupportUkraine](https://github.com/vshymanskyy/StandWithUkraine))

## Installation (Homebrew)

You can install CrossCast using Homebrew:

```
brew install --formula ./Formula/crosscast.rb
```

Or run directly with Python 3:

```
python3 crosscast/crosscast.py <command> [options]
```

## Usage

### Send a file
```
crosscast send <receiver_ip> <port> <file_path>
```

### Receive a file
```
crosscast receive <port> [output_directory]
```

### Find receivers
```
crosscast find [--port PORT] [--timeout SECONDS]
```

### Show help
```
crosscast help
```

### Easter egg
```
crosscast easteregg
```

## Example
On receiver (Mac/Linux):
```
crosscast receive 9000
```

On sender (Windows):
```
python3 crosscast/crosscast.py send 192.168.1.10 9000 myfile.txt
```

## Note
- Both sender and receiver must be on the same network.
- For Windows, use Python 3 and run from Command Prompt or PowerShell.

## Support

For support, please leave a issue in the issues tab


## Used By

This project isn't in use by any type of company, but you could be the first!!

## We Support Ukraine

This project stands in solidarity with Ukraine. See the [#WeSupportUkraine GitHub repository](https://github.com/vshymanskyy/StandWithUkraine) for more information and ways to help.

[![We Support Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/WeSupportUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine)
