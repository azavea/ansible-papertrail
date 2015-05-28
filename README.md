# ansible-papertrail
An ansible role for installing [Papertrail](https://papertrailapp.com).

## Role Variables

- `papertrail_version` - Release of Papertrail's [remote_syslog2](https://github.com/papertrail/remote_syslog2) to use
- `papertrail_check_interval_s` - Interval in seconds to check the logs (defaults to 10s)
- `papertrail_port` - Must be set to user's Papertrail port
- `papertrail_log_files` - List of logfiles to send; defaults to all .log files in /var/log

## Example Playbook

See the [examples](./examples/) directory.
