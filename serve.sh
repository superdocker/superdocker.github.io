#!/bin/bash
PID_FILE=".jekyll.pid"

if [ -f "$PID_FILE" ] && kill -0 "$(cat $PID_FILE)" 2>/dev/null; then
  echo "Jekyll is already running (PID $(cat $PID_FILE))"
  exit 0
fi

bundle exec jekyll serve > /tmp/jekyll.log 2>&1 &
echo $! > "$PID_FILE"
echo "Jekyll starting... (PID $!)"

until grep -q "Server running" /tmp/jekyll.log 2>/dev/null || grep -q "Error:" /tmp/jekyll.log 2>/dev/null; do
  sleep 2
done

if grep -q "Server running" /tmp/jekyll.log; then
  echo "Server running at http://localhost:4000"
else
  echo "Failed to start Jekyll:"
  grep "Error:" /tmp/jekyll.log
  rm -f "$PID_FILE"
  exit 1
fi
