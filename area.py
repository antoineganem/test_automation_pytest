def calculate_triangle_area(base, height):
  if base <= 0:
    raise ValueError("Base must be greater than zero.")

  if height < 0:
    raise ValueError("Height cannot be negative.")

  return 0.5 * base * height

