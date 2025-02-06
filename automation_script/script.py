import os
import psutil
import json
from datetime import datetime

def get_system_health():
    """Collect basic system health metrics."""
    return {
        'timestamp': datetime.now().isoformat(),
        'cpu_usage': psutil.cpu_percent(),
        'memory': {
            'total': psutil.virtual_memory().total / (1024 * 1024 * 1024),  # GB
            'used_percent': psutil.virtual_memory().percent
        },
        'disk': {
            'total': psutil.disk_usage('/').total / (1024 * 1024 * 1024),  # GB
            'used_percent': psutil.disk_usage('/').percent
        },
        'running_processes': len(psutil.pids())
    }

def save_report(health_data):
    """Save health report to a JSON file."""
    os.makedirs('reports', exist_ok=True)
    filename = f'reports/health_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    
    with open(filename, 'w') as f:
        json.dump(health_data, f, indent=4)
    
    print(f"Report saved: {filename}")

def main():
    """Main function to run system health check."""
    health_report = get_system_health()
    save_report(health_report)
    print(json.dumps(health_report, indent=2))

if __name__ == '__main__':
    main()