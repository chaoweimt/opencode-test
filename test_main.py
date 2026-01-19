import io
import sys
from main import hello_world


def test_hello_world_output():
    """Test that hello_world prints the correct message."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    hello_world()
    
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Hello, World!\n"


def test_hello_world_returns_none():
    """Test that hello_world returns None."""
    result = hello_world()
    assert result is None
