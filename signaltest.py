import signal

# Define a signal handler function
def signal_handler(signum, frame):
    print(f"\nReceived signal {signum} so elegantly ending the program")

# Register the signal handler for the SIGINT signal (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Wait for a signal to be received
print("Waiting for signal...")
signal.pause()