def monitor_logs(file_path):
    print(f"--- Scanning Log File: {file_path} ---")
    with open(file_path, 'r') as file:
        for line in file:
            if "FAILED LOGIN" in line or "UNAUTHORIZED" in line:
                print(f"[!] SECURITY ALERT: {line.strip()}")

monitor_logs('access_log.txt')
