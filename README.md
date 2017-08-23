# ansible-papertrail

An Ansible role for installing [Papertrail](https://papertrailapp.com).

## Role Variables

- `papertrail_version` - Release of [remote_syslog2](https://github.com/papertrail/remote_syslog2) to use
- `papertrail_conf` - Application logs configuration file (default: `/etc/log_files.yml`)
- `papertrail_host` - Host for Papertrail's logging endpoint (default: `logs2.papertrail.com`)
- `papertrail_port` - Port for Papertrail's logging endpoint (default: `45551`)
- `papertrail_preserve_fqdn` - Configure if rsyslog need to respect FQDN (default: `off`)

## Usage

Ensure that `papertrail_host` and `papertrail_port` are set to the endpoints provided to your account by Papertrail. Both can be found in the user [account settings](https://papertrailapp.com/systems/setup).

In addition, this role does not attempt to setup any configuration for application logs. Only system logs are shipped to Papertrail by default (via Rsyslog). If you want to ship a custom set of application logs, wrap this role with a project specific role that templates the `papertrail_conf` file. Generally, this is `/etc/log_files.yml` and looks like this inside:

```yaml
files:
  - /var/log/httpd/access_log
  - /var/log/httpd/error_log
  - /opt/misc/*.log
  - /home/**/*.log
  - /var/log/mysqld.log
  - /var/run/mysqld/mysqld-slow.log
exclude_files:
  - old
  - 200\d
hostname: www42  # override OS hostname
exclude_patterns:
  - exclude this
  - \d+ things
destination:
  host: logs.papertrailapp.com
  port: 12345   # NOTE: change this to YOUR papertrail port!
  protocol: tls
new_file_check_interval: "10" # Check every 10 seconds
```

## Testing
Tests are done using [molecule](http://molecule.readthedocs.io/). To run the test suite, install molecule and its dependencies and run ` molecule test` from the folder containing molecule.yml. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) python script in the [tests](./tests/) directory, or add a function to [test_papertrail.py](./tests/test_papertrail.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Example
```
# Download molecule, dependencies
$ pip install molecule

# Change to the top-level project directory, which contains molecule.yml
$ cd /path/to/ansible-papertrail

# Ensure that molecule.yml is present
$ ls
CHANGELOG.md                             molecule.yml
LICENSE                                  playbook.retry
README.md                                playbook.yml
ansible.cfg                              tasks
defaults                                 templates
handlers                                 tests
meta

# We're in the right directory, so let's run tests!
$ molecule test
```