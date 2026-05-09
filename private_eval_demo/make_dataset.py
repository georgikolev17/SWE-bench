import json
from pathlib import Path

patch = Path("private_eval_demo/gold.patch").read_text(encoding="utf-8")

instance = {
    "instance_id": "georgikolev17__eval_regress_test-2",
    "repo": "georgikolev17/eval_regress_test",
    "base_commit": "4b54fd6813fa8ce88cafb3c89dde9e2d8b84b30d",
    "patch": patch,
    "test_patch": "",
    "problem_statement": """`count_up_to` excludes the limit value

The function is expected to include the upper bound in the returned sequence.
Expected behavior: count_up_to(4) returns [1, 2, 3, 4].
Actual behavior: count_up_to(4) returns [1, 2, 3].
Acceptance criteria: Returned list includes limit when limit >= 1.
Affected function: count_up_to
""",
    "version": "demo",
    "issue_numbers": [2],
    "FAIL_TO_PASS": ["test_app.py::test_count_up_to_includes_limit"],
    "PASS_TO_PASS": [],
}

Path("private_eval_demo/dataset.jsonl").write_text(
    json.dumps(instance) + "\n",
    encoding="utf-8",
)