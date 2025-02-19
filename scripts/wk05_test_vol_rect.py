def volume_rect(l, w, h):
    return l * w * h

def test_volume_rect():
  assert volume_rect(2.0 ,3 , 4) == 24.0, "volume calculation error"
  assert type(volume_rect(2.0,3,4)) == float, "volume function error; when one of the input is in float type, the product should be in float type."

test_volume_rect()