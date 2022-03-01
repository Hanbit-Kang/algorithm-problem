# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

def is_a_and_b_valid(a, b):
  for i in range(N-1):
    if(nums[i]*a + b != nums[i+1]):
      return False

  return True

if __name__ == '__main__':
  N = int(input())
  nums = list(map(int, input().split()))
  if(N <= 2):
    if(N == 2 and nums[0] == nums[1]):
      # ex. [57, 57]
      print(nums[0])
    else:
      # �Ϲ����� ���
      print("A")
  else:                             
    if(nums[0] == nums[1]):    
      # ex. [57, 57, ...]
      a = 0
      b = nums[0]
    else:
      # �Ϲ����� ���
      # nums[0]*a + b = nums[1]
      # nums[1]*a + b = nums[2]
      # ����, (nums[1] - nums[0])*a = nums[2] - nums[1]�̰�, �̸� �����ϸ�
      # a = (nums[2] - nums[1]) / (nums[1] - nums[0])�̴�.
      a = int((nums[2] - nums[1]) / (nums[1] - nums[0]))
      b = nums[1] - nums[0]*a    
      
    if(is_a_and_b_valid(a, b)):
      print(nums[-1]*a + b)
    else:
      print("B")