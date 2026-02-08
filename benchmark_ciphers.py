import paho.mqtt.client as mqtt
import ssl
import time
import psutil
# --- Configuration ---
BROKER_ADDRESS = "test.mosquitto.org"
TLS_PORT = 8883 # Standard TLS port for MQTT

# ECC-based suite
CIPHER_SUITE_ECC = "ECDHE-ECDSA-AES128-GCM-SHA256"
#RSA-based suite
CIPHER_SUITE_RSA = "AES256-GCM-SHA384" 

# List of ciphers to test
CIPHERS_TO_TEST = [CIPHER_SUITE_ECC, CIPHER_SUITE_RSA]

def measure_handshake_time(cipher):
    client = mqtt.Client()
    # Configure TLS context to use ONLY the specified cipher
    client.tls_set(
        tls_version=ssl.PROTOCOL_TLS,
        ciphers=cipher,
        cert_reqs=ssl.CERT_NONE
    )
    start_time = 0
    end_time = 0
    try:
        # Record time just before initiating the connection
        start_time = time.monotonic()
        client.connect(BROKER_ADDRESS, TLS_PORT, 60)
        # The handshake is complete once connect() returns without error
        end_time = time.monotonic()

        client.disconnect()
        # Return duration in milliseconds
        return (end_time - start_time) * 1000
    except Exception as e:
        print(f"Failed to connect with {cipher}: {e}")
        return None

# --- Main Execution ---
if __name__ == "__main__":
    NUMBER_OF_RUNS = 10 # Run each test 10 times for a stable average

    for cipher in CIPHERS_TO_TEST:
        print(f"--- Testing Cipher: {cipher} ---")
        timings = []
        for i in range(NUMBER_OF_RUNS):
            duration = measure_handshake_time(cipher)
            if duration:
                print(f"Run {i+1}: {duration:.2f} ms")
                timings.append(duration)
            time.sleep(1) # Pause briefly between connections

        if timings:
            average_time = sum(timings) / len(timings)
            print(f"\n[RESULT] Average handshake time for {cipher}: {average_time:.2f} ms\n")

