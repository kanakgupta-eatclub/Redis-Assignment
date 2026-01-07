import time
from rate_limiter import RateLimiter

rate_limiter = RateLimiter()

ip = "1.1.1.1"
route = "/order"
max_requests = 3
window_seconds = 10

print("Sending requests...\n")

for i in range(1, 6):
    allowed = rate_limiter.allow_request(
        ip_address=ip,
        api_route=route,
        max_requests=max_requests,
        window_seconds=window_seconds
    )

    status = "ALLOWED" if allowed else "BLOCKED"
    print(f"Request {i}: {status}")
    time.sleep(2)

print("\nWaiting for window to expire...\n")
time.sleep(5)

allowed = rate_limiter.allow_request(
    ip_address=ip,
    api_route=route,
    max_requests=max_requests,
    window_seconds=window_seconds
)

print(f"After window reset: {'ALLOWED' if allowed else 'BLOCKED'}")
