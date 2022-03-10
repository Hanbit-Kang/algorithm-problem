# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
input = sys.stdin.readline

if __name__ == '__main__':
  N, K = map(int, input().split())       
  sums = []
  cur_sum = 0
  for num in map(int, input().split()):
    cur_sum += num
    sums.append(cur_sum)

  mp = defaultdict(int)
  res = 0
  for sm in sums:
    if sm == K:
      res += 1
          
    # (���ϰ��� �ϴ� ������) = (���� ������) - (������ � ������) = K
    res += mp[sm-K]
    mp[sm] += 1

  print(res)