import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_report_exists():
    """Verifies success criterion 1: report.json is a valid JSON object."""
    assert REPORT_PATH.is_file(), "no report.json found"

    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AssertionError(f"report.json is not valid UTF-8 JSON: {exc}") from exc

    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_has_exact_keys():
    """Verifies success criterion 2: the JSON object has exactly the required keys."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies success criterion 3: total_requests is the correct integer count."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert type(report["total_requests"]) is int
    assert report["total_requests"] == EXPECTED_REPORT["total_requests"]


def test_unique_ips():
    """Verifies success criterion 4: unique_ips is the correct integer count."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert type(report["unique_ips"]) is int
    assert report["unique_ips"] == EXPECTED_REPORT["unique_ips"]


def test_top_path():
    """Verifies success criterion 5: top_path is the correct string path."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert type(report["top_path"]) is str
    assert report["top_path"] == EXPECTED_REPORT["top_path"]
