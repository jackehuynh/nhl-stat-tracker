from click.testing import CliRunner
from team_info import *

def test_info():
    runner = CliRunner()
    result = runner.invoke(get_team_info(), ['sjs'])
    result2 = runner.invoke(write_info_to_file(), ['sjs', 'test.txt'])
    assert result.exit_code == 0
    assert result.output == result2.output