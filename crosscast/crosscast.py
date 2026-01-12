#!/usr/bin/env python3
import argparse
import socket
import os

def send_file(ip, port, filepath):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                s.sendall(data)
    print(f"Sent {filepath} to {ip}:{port}")

def receive_file(port, outdir):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.listen(1)
        print(f"Waiting for file on port {port}...")
        conn, addr = s.accept()
        with conn:
            filename = f"received_{addr[0]}_{port}"
            outpath = os.path.join(outdir, filename)
            with open(outpath, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
            print(f"Received file saved to {outpath}")


def find_receivers(port=9000, timeout=3):
    """Broadcasts on the local network to find receivers."""
    message = b'CROSSCAST_DISCOVER'
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.settimeout(timeout)
        s.sendto(message, ("255.255.255.255", port))
        print(f"Broadcasting for receivers on port {port}...")
        try:
            while True:
                data, addr = s.recvfrom(1024)
                if data == b'CROSSCAST_HERE':
                    print(f"Found receiver at {addr[0]}:{addr[1]}")
        except socket.timeout:
            print("Discovery finished.")

def receiver_announce(port):
    """Listens for discovery broadcasts and responds."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(("", port))
        while True:
            data, addr = s.recvfrom(1024)
            if data == b'CROSSCAST_DISCOVER':
                s.sendto(b'CROSSCAST_HERE', addr)

def main():
    parser = argparse.ArgumentParser(description="CrossCast: Simple cross-platform file transfer tool.")
    subparsers = parser.add_subparsers(dest="command")

    send_parser = subparsers.add_parser("send", help="Send a file")
    send_parser.add_argument("ip", help="Receiver IP address")
    send_parser.add_argument("port", type=int, help="Port to use")
    send_parser.add_argument("filepath", help="Path to file to send")

    recv_parser = subparsers.add_parser("receive", help="Receive a file")
    recv_parser.add_argument("port", type=int, help="Port to listen on")
    recv_parser.add_argument("outdir", default=".", nargs="?", help="Directory to save received file")

    find_parser = subparsers.add_parser("find", help="Find receivers on the local network")
    find_parser.add_argument("--port", type=int, default=9000, help="Port to broadcast on")
    find_parser.add_argument("--timeout", type=int, default=3, help="Discovery timeout in seconds")


    help_parser = subparsers.add_parser("help", help="Show help message")

    easteregg_parser = subparsers.add_parser("easteregg", help="Show a fun CrossCast easter egg!")

    args = parser.parse_args()
    if args.command == "send":
        send_file(args.ip, args.port, args.filepath)
    elif args.command == "receive":
        import threading
        # Start receiver announce in background for discovery
        t = threading.Thread(target=receiver_announce, args=(args.port,), daemon=True)
        t.start()
        receive_file(args.port, args.outdir)
    elif args.command == "find":
        find_receivers(args.port, args.timeout)
    elif args.command == "easteregg":
        print("\n🐧✨ You found the CrossCast Easter Egg! ✨🍏\n")
        print("Did you know? CrossCast was built to bring all platforms together—just like this little surprise!\n")
        print("Share files, share joy, and remember: tech is better when it connects us all.\n")
        print("#WeSupportUkraine 💙💛\n")
    elif args.command == "help" or args.command is None:
        parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
