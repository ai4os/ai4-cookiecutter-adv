import pytest


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_git_base_url(project, git_base_url):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_project_name(project, project_name):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_author_name(project, author_name):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_author_email(project, author_email):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_description(project, description):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_app_version(project, app_version):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_open_source_license(project, open_source_license):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_dockerhub_user(project, dockerhub_user):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_docker_baseimage(project, docker_baseimage):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_baseimage_cpu_tag(project, baseimage_cpu_tag):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_baseimage_gpu_tag(project, baseimage_gpu_tag):
    raise NotImplementedError  # TODO: implement your test here


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_failure_notify(project, failure_notify):
    raise NotImplementedError  # TODO: implement your test here
