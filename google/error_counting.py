logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: Page loaded",
    "ERROR: Timeout reached",
    "DEBUG: Cache cleared",
    "ERROR: Invalid password"
]

def find_errors(log_list):
    for line in log_list:
        if "ERROR" in line:
            yield line

error_counter = 0

for error in find_errors(logs):
    print(f"Найдена проблема: {error}")
    error_counter += 1

print(f"--- Итого найдено ошибок: {error_counter} ---")