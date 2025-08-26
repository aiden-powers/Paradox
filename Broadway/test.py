from datetime import datetime, timezone

# Get current UTC time with timezone information
now_utc = datetime.now(timezone.utc)

# Format to ISO 8601 and replace +00:00 with Z
iso_z_format = now_utc.isoformat(timespec='milliseconds').replace('+00:00', 'Z')

print(iso_z_format)