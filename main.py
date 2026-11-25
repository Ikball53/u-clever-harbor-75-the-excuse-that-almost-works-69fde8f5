"""The Excuse That Almost Works -- make.fun one-liner entry.

Writes the single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import tempfile

LINE = "Dentist moved my root canal to 9am Friday, only slot this month, and I can't exactly reschedule a drill."

# The brief caps the line at 20 words and the gate caps output at 140 chars.
# Enforce both here so a bad edit fails loudly instead of shipping.
assert len(LINE) <= 140, "line exceeds 140 characters"
assert len(LINE.split()) <= 20, "line exceeds 20 words"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
