#!/bin/bash
(&>/dev/null python /app/main.py)&
socat - TCP:127.0.0.1:5000,forever