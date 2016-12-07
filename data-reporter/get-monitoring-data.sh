#!/bin/sh

ssh beehive "sqlite3 /var/lib/monitoring/monitor.db 'SELECT * FROM updates;'"
