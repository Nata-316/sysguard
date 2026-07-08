"""
Single source of truth for alert thresholds.

logger.py and alerts.py both read from here instead of hardcoding their
own numbers. This is what stops the two files from silently drifting out
of sync — which is how the `memory_usage['percent'] > 1` bug in alerts.py
went unnoticed: nothing forced the two threshold sets to agree.

Fill in the values below.
"""

CPU_WARNING_THRESHOLD = 90          # percent
MEMORY_WARNING_THRESHOLD = 85       # percent
DISK_WARNING_THRESHOLD = 90         # percent

# NOTE: net_io_counters() is cumulative since boot, not per-interval.
# Comparing it directly against a flat MB threshold is the network bug
# we're tackling next. Any number here would be meaningless until that's
# fixed — a "sent > X MB" check against a cumulative counter trips once,
# shortly after boot, and then stays tripped forever. Left unset on
# purpose; set this once check_alerts() is measuring a delta instead.
NETWORK_SENT_WARNING_THRESHOLD = None   # MB per interval
NETWORK_RECV_WARNING_THRESHOLD = None   # MB per interval
