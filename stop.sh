#!/bin/bash
PID_FILE=".jekyll.pid"

if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
    echo "Jekyll stopped (PID $PID)"
  else
    echo "Jekyll is not running"
  fi
  rm -f "$PID_FILE"
else
  pkill -f "jekyll serve" 2>/dev/null && echo "Jekyll stopped" || echo "Jekyll is not running"
fi
