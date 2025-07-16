from flask_limiter import Limiter
from utils.auth import get_user_or_ip

# Create a limiter instance that can be imported anywhere
limiter = Limiter(
    key_func=get_user_or_ip,
    default_limits=["100 per hour"],
    storage_uri="memory://",
)
