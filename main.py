def diff(angle1, angle2):
  """
  The function takes two angles (int) with values ranging from 0 to 360, and returns the smallest difference between them
  """
  angle_difference = abs((angle1 - angle2) % 360)
  max_angle = max(angle1 % 360, angle2 % 360)
  min_angle = min(angle1 % 360, angle2 % 360)
  if angle_difference < 180:
    return angle_difference
  return 360 - max_angle + min_angle

