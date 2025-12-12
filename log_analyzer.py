import re
from collections import Counter

def read_log(file):
    """Reads all lines from the log file"""
    with open(file, "r") as f:
        return f.readlines()


def count_errors(lines):
    """Counts number of ERROR / WARNING / INFO"""
    error_count = sum(1 for line in lines if "ERROR" in line)
    warn_count = sum(1 for line in lines if "WARNING" in line)
    info_count = sum(1 for line in lines if "INFO" in line)

    return error_count, warn_count, info_count


def extract_ips(lines):
    """Extracts all IP addresses from log lines"""
    ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
    ips = re.findall(ip_pattern, "".join(lines))
    return Counter(ips)


def most_frequent_errors(lines, top_n=5):
    """Finds most common error messages"""
    errors = [line.strip() for line in lines if "ERROR" in line]
    return Counter(errors).most_common(top_n)


def log_summary(file):
    """Main analysis function"""
    lines = read_log(file)

    error_count, warn_count, info_count = count_errors(lines)
    ip_counts = extract_ips(lines)
    frequent_errors = most_frequent_errors(lines)

    print("\n========== LOG ANALYZER REPORT ==========")
    print(f"Total log lines: {len(lines)}")
    print(f"INFO messages: {info_count}")
    print(f"WARNING messages: {warn_count}")
    print(f"ERROR messages: {error_count}")

    print("\n--- Top IP Addresses ---")
    for ip, count in ip_counts.most_common(5):
        print(f"{ip} → {count} times")

    print("\n--- Most Frequent Errors ---")
    for err, count in frequent_errors:
        print(f"{count}x → {err}")

    print("=========================================\n")


if __name__ == "__main__":
    filename = input("Enter log file name: ")
    log_summary(filename)
