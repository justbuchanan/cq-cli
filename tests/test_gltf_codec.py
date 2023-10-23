import pytest
import tests.test_helpers as helpers


@pytest.mark.skip(
    reason="Waiting on #1414 on the CadQuery repo to be merged to finish this"
)
def test_gltf_codec():
    """
    Basic test of the GLTF codec plugin.
    """
    test_file = helpers.get_test_file_location("cube_assy.py")

    command = ["python", "cq-cli.py", "--codec", "gltf", "--infile", test_file]
    out, err, exitcode = helpers.cli_call(command)

    assert out.decode().split("\n")[0].replace("\r", "").startswith('{"accessors":')
