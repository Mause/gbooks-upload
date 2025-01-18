from click.testing import CliRunner

from upload import main as upload


def test_hello_world(snapshot):
    runner = CliRunner()
    result = runner.invoke(upload, ["--help"])
    assert result.exit_code == 0
    assert result.output == snapshot
