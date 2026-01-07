# Redis-Based Fixed Window Rate Limiter (POC)

## Objective
Implement a Redis-backed **fixed window rate limiter** that restricts the number of requests allowed per **IP address** and **API route** within a fixed time window.

---

## Tech Stack
- **Python 3**
- **Redis (local instance)**
- **redis-py client**

---

## Redis Key Design

The rate limiter uses a single Redis key per **IP address and API route** combination to track request counts.

### Key Format - rate_limit:{ip_address}:{api_route}

Each key stores an **integer counter** representing the number of requests made by a specific IP to a specific API route within the current fixed time window.

This design ensures:
- Independent rate limiting per IP
- Independent rate limiting per API route
- No interference between different clients or endpoints

---

## Expiration Handling

Expiration is handled using Redis’s built-in **Time-To-Live (TTL)** mechanism.

- When the **first request** for a given key is received:
  - The counter is initialized using the `INCR` command
  - A TTL equal to `window_seconds` is set using the `EXPIRE` command
- Redis automatically deletes the key once the TTL expires
- When the key is deleted:
  - The request count is reset
  - The next incoming request starts a new fixed window

This approach ensures:
- Automatic window reset
- No manual cleanup logic
- Correct fixed window behavior

---

## Assumptions


- Network failures, Redis restarts, and distributed consistency are not handled

