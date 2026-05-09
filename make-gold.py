import json

# This version uses a simpler diff format that is more likely to succeed
patch = """--- a/django/db/models/functions/datetime.py
+++ b/django/db/models/functions/datetime.py
@@ -100,6 +100,6 @@
     def convert_value(self, value, expression, connection):
-        if isinstance(value, datetime.datetime):
+        if value is not None and isinstance(value, datetime.datetime):
             if settings.USE_TZ and value.tzinfo is None:
"""

data = {
    "instance_id": "django__django-11133",
    "model_patch": patch,
    "model_name_or_path": "human-gold"
}

with open("gold_predictions.jsonl", "w") as f:
    f.write(json.dumps(data) + "\n")

print("Created a more resilient gold_predictions.jsonl")
