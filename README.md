# ansible-papertrail
An ansible role for installing [Papertrail](https://papertrailapp.com).

## Role Variables

- `papertrail_version` - Release of Papertrail's [remote_syslog2](https://github.com/papertrail/remote_syslog2) to use
- `papertrail_check_interval_s` - Interval in seconds to check the logs (defaults to 10s)
- `papertrail_host` - Must be set to the user's Papertrail logging subdomain
- `papertrail_port` - Must be set to user's Papertrail port
- `papertrail_log_files` - List of logfiles to send; defaults to all .log files in /var/log

## Usage
The `papertrail_host` and `papertrail_port` must be set to the subdomain and port for the user account to receive the logs.  Both may be found in the user's [account settings](https://papertrailapp.com/systems/setup).
You will probably want to change `papertrail_log_files` to only send logs of interest; by default,
it will send quite a lot of data.

## Example Playbook

See the [examples](./examples/) directory.
