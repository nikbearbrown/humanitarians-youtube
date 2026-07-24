# PEDAGOGY — fluency-correctness-gap

## Concept

Fluency-correctness gap: passing tests do not equal correct code.

## Question

What is the fluency-correctness gap?

## Answer

Claude's output is optimized for fluency, not correctness. Its self-generated tests probe the dimensions it modeled confidently — not the dimensions where the bug lives. The student must add the probe Claude cannot generate for itself: the test case that exposes the failure mode Claude's fluency masked.

## Key Insight: The self-consistent error

When Claude generates both the function and the tests, both sides share the same production failure mode. The test suite is self-consistent and wrong: it tests what Claude knew to test (the happy path) and misses what Claude didn't know it didn't know (the tie case). A 100% pass rate on a self-generated test suite is evidence about what Claude modeled confidently — nothing more.

## The correct probe

The probe the student must add:
```python
def test_tie_breaking():
    students = [
        {'name': 'Bell', 'gpa': 3.92, 'last_name': 'Bell'},
        {'name': 'Adams', 'gpa': 3.92, 'last_name': 'Adams'},
        {'name': 'Chen', 'gpa': 3.85, 'last_name': 'Chen'},
    ]
    result = top_three_by_gpa(students)
    assert result[0]['last_name'] == 'Adams'  # alphabetical tie-break
```

## Source

Chapter 02: Division of Labor — claude-code-for-students
Kahneman 2011 "Thinking, Fast and Slow" — System 1/System 2 framing
Pearce et al. 2022 "Asleep at the Keyboard" — self-audit limitation
