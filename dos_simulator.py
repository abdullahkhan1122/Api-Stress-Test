import requests
import threading
import time
import statistics  # For average time calc

URL = "http://localhost:5000/rick"  # Target the funny endpoint
NUM_THREADS = 300  # High for stress - adjust if your PC can't handle
TIMEOUT = 10  # Seconds before giving up on a request

def send_request(response_times):
    start = time.time()
    try:
        r = requests.get(URL, timeout=TIMEOUT)
        elapsed = time.time() - start
        response_times.append(elapsed)
        print(f"Success! Status: {r.status_code} | Time: {elapsed:.2f}s")
    except requests.exceptions.RequestException as e:
        elapsed = time.time() - start
        response_times.append(elapsed)
        print(f"Failed: {e} | Time: {elapsed:.2f}s (likely DoS)")

if __name__ == "__main__":
    print("="*60)
    print(f"Starting STRESS TEST: {NUM_THREADS} requests incoming!")
    print("Watch the server terminal for overload...")
    print("="*60)
    
    threads = []
    response_times = []  # Track times for summary
    
    overall_start = time.time()
    
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=send_request, args=(response_times,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    overall_end = time.time()
    
    if response_times:
        avg_time = statistics.mean(response_times)
        max_time = max(response_times)
    else:
        avg_time = "N/A"
        max_time = "N/A"

    print("="*60)
    print(f"STRESS TEST COMPLETE")
    print(f"Total time: {overall_end - overall_start:.2f}s")
    print(f"Avg response: {avg_time:.2f}s")
    print(f"Max response: {max_time:.2f}s")
    print("If vulnerable: Times are HUGE | If protected: Many failures but fast survivors")
    print("="*60)