# Status online, offline
import pytest


def count_status(statuses: dict, status) -> int:
    return list(statuses.values()).count(status)


class TestOnlineStatuses:
    @pytest.fixture
    def statuses(self):
        s = {
            "Alice": "online",
            "Bob": "offline",
            "Eve": "online",
            "Charlie": "offline",
            "Simon": "online",
            "Edward": "online",
            "Sahra": "offline",
        }
        return s

    def test_correct_statuses(self, statuses):
        assert count_status(statuses, "online") == 4
        assert count_status(statuses, "offline") == 3
        assert count_status(statuses, "xxx") == 0
