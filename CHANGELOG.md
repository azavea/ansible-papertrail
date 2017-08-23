## 1.2.0

- Use `get_url` checksum argument instead of deprecated sha256sum.
- Extract `remote_syslog` if a new version has been downloaded.
- Add support for Ubuntu 16.04.

## 1.1.2

- Add dependency metadata to role.

## 1.1.1

- Update checksum for Papertrail certificate.

## 1.1.0

- Add support for `PreserveFQDN` Rsyslog configuration setting.

## 1.0.0

- Bump `remote_syslog2` version to `0.15`.
- Push responsibility of `log_files.yml` creation to user.
- Configure Rsyslog to queue requests when offline.
- Configure Papertrail log shipping via Rsyslog via `/etc/rsyslog.d`.

## 0.1.0

- Initial release.
