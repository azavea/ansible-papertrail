import pytest
import re


@pytest.fixture()
def AnsibleDefaults(Ansible):
    """ Load default variables into dictionary.
    Args:
        Ansible - Requires the ansible connection backend.
    """
    return Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]


def test_papertrail_user(User):
    """Check that the Papertrail user exists with the right configuration"""
    papertrail = User('papertrail')
    assert papertrail.exists
    assert papertrail.home == "/var/lib/papertrail"
    assert papertrail.shell == "/bin/false"
    assert papertrail.name == "papertrail"


def test_papertrail_bundle(File):
    """Check that the Papertrail certificate bundle exists"""
    assert File('/etc/papertrail-bundle.pem').exists


def test_rsyslog_gnutils(Package):
    """Check that the rsyslog TLS support is installed"""
    assert Package("rsyslog-gnutls").is_installed


def test_services(Service):
    """Check that syslog/remote syslog are running"""
    assert Service("rsyslog").is_enabled
    assert Service("remote_syslog").is_enabled


def test_papertrail_configuration(File, AnsibleDefaults):
    """Check make sure the proper Papertrail configuration exists"""
    papertrail_config = File(AnsibleDefaults["papertrail_conf"])
    papertrail_host = AnsibleDefaults["papertrail_host"]
    papertrail_port = AnsibleDefaults["papertrail_port"]

    assert papertrail_config.exists
    assert re.search("host: {}".format(papertrail_host),
                     papertrail_config.content_string) is not None
    assert re.search("port: {}".format(papertrail_port),
                     papertrail_config.content_string) is not None


def test_rsyslog_configuration(File, AnsibleDefaults):
    """Check make sure the proper rsyslog configuration exists"""
    rsyslog_config = File("/etc/rsyslog.d/90-papertrail.conf")
    papertrail_host = AnsibleDefaults["papertrail_host"]
    papertrail_port = AnsibleDefaults["papertrail_port"]

    assert rsyslog_config.exists
    assert re.search("\*\.\* @@{}:{}".format(papertrail_host, papertrail_port),
                     rsyslog_config.content_string) is not None
