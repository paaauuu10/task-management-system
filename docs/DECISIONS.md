[DECISION 1]

Decision: Use python:3.11-slim as the base image.
Reasoning:
    · It is an official Python image, maintained by the Python/Docker teams.
    · The slim variant is significantly smaller than the full Debian-based image, which reduces build times and final image size.

[DECISION 2]

Decision: Use psycopg2-binary
Reasoning: 
    · This avoids the need for compilation or installing extra system libraries.

