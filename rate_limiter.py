import redis

class RateLimiter:
    def __init__(self, redis_host="localhost", redis_port=6379, db=0):
        self.redis = redis.Redis(
            host=redis_host,
            port=redis_port,
            db=db,
            decode_responses=True
        )

    def allow_request(self, ip_address, api_route, max_requests, window_seconds):
        """
        Returns True if request is allowed
        Returns False if request should be blocked
        """

        # Redis key per IP + route
        key = f"rate_limit:{ip_address}:{api_route}"

        # Increment request count
        current_count = self.redis.incr(key)

        # If this is the first request, set expiration
        if current_count == 1:
            self.redis.expire(key, window_seconds)

        # Check limit
        if current_count > max_requests:
            return False

        return True
