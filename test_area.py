import pytest
from area import calculate_triangle_area

def test_valid_area():
  assert calculate_triangle_area(5, 7) == 17.5

def test_negative_base():
  with pytest.raises(ValueError, match="Base must be greater than zero."):
    calculate_triangle_area(-5, 7)

def test_negative_height():
  with pytest.raises(ValueError, match="Height cannot be negative."):
    calculate_triangle_area(5, -7)
    
def test_zero_base():
  with pytest.raises(ValueError, match="Base must be greater than zero."):
    calculate_triangle_area(0, 7)