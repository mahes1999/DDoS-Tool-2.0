import socket
import time
import threading
import random

# Set the target server's IP address and port
target_ip = "127.0.0.1"
target_port = 80

# Set the number of connections to simulate
num_connections = 500

# Set the duration of the test (in seconds)
test_duration = 60

# Set the packet size (in bytes)
packet_size = 1024

# Create a lock for threading
lock = threading.Lock()

# Function to send traffic to the target server
def send_traffic():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_ip, target_port))
    while True:
        packet = bytes([random.randint(0, 255) for _ in range(packet_size)])
        sock.send(packet)
        lock.acquire()
        global bytes_sent
        bytes_sent += packet_size
        lock.release()

# Create and start the threads
threads = []
for i in range(num_connections):
    thread = threading.Thread(target=send_traffic)
    thread.start()
    threads.append(thread)

# Wait for the test duration
time.sleep(test_duration)

# Stop the threads and close the sockets
for thread in threads:
    thread.join()
    sock.close()

# Print the results
print(f"Bytes sent: {bytes_sent}")
print(f"Connections: {num_connections}")
print(f"Duration: {test_duration} seconds")

