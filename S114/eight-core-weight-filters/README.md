# Eight-core weight filters

Start with `RESULT.md`. Full labelled core inputs and exact certificates are included.

Run standard-library verification:

```
python verify.py
python validate_inflations.py
python verify_families.py
```

Results: 57 necessary inequalities for 17 frozen eight-point cores; four additional minimal linear singleton clauses across C06/C10/C13; exact bounded-family exclusions requiring an additional nonsingleton beyond the old port-forced set in every class. No complete core is excluded for every positive weight vector.
