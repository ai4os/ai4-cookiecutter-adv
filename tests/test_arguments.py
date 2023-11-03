import pytest


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_git_base_url(pyproject, git_base_url, package_slug):
    urls = pyproject["project"]["urls"]
    assert urls["Homepage"] == f"{git_base_url}/{package_slug}"
    assert urls["Bug Tracker"] == f"{git_base_url}/{package_slug}/issues"


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_project_name(pyproject, model_name):
    correct_name = model_name.lower().replace(" ", "-") + "-api"
    assert pyproject["project"]["name"] == correct_name


@pytest.mark.parametrize("config_file", ["config-1"], indirect=True)
def test_pyproject_authors(pyproject):
    assert pyproject["project"]["authors"] == [
        {"name": "VK", "email": "v.k@example.com"},
        {"name": "BE", "email": "b.e@example.com"},
    ]


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_description(pyproject, description):
    assert pyproject["project"]["description"] == description


@pytest.mark.parametrize("config_file", ["config-1", "config-2"], indirect=True)
def test_app_version(project, app_version):
    with open(project / "VERSION", "r", encoding="utf-8") as file:
        assert file.read().rstrip() == app_version


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
