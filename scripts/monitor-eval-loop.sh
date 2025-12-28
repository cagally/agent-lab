#!/bin/bash
# Monitor evaluation progress every 5 minutes

while true; do
    echo ""
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Checking progress..."
    python3.11 /home/ubuntu/agent-lab/scripts/check-eval-progress.py
    
    # Check if process is still running
    if ps aux | grep "run-api-tests-v2-fixed.py" | grep -v grep > /dev/null; then
        echo "✓ Evaluation process is running"
    else
        echo "✗ Evaluation process has stopped"
        break
    fi
    
    # Check log for recent activity
    echo ""
    echo "Recent log activity:"
    tail -n 5 /home/ubuntu/agent-lab/evaluations/eval-run.log
    
    echo ""
    echo "Waiting 5 minutes before next check..."
    sleep 300
done

echo ""
echo "Monitoring stopped - evaluation process not running"
