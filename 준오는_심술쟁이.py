# -*- coding: utf-8 -*-
import sys                           
input = sys.stdin.readline       
INF = 1000000007
                           
if __name__ == '__main__':
  s = int(input())            
  n = len(str(input().rstrip()))      
                               
  dp = [0]*(s+1) # dp[k]: k��ŭ �ٲ��� ���� ����� ��
  dp[0] = 1
  next_dp = [0]*(s+1)

  for _ in range(n):                      
    prefix_sum = 0

    for k in range(s+1):     
      prefix_sum = (prefix_sum + dp[k]) % INF
      if k > 25: # 1 <= k <= 25(���� ����)�̹Ƿ� �κ����� ������ ��������
        prefix_sum = (prefix_sum - dp[k-26] + INF) % INF

      next_dp[k] = prefix_sum

    # dp�� next_dp���� ����Ű�� �ϱ� ���� �����͸� �������ش�.
    # ������ next_dp�� �ʱⰪ�� ������� ���ŵǹǷ� dp�� ������ ��� ����.
    dp, next_dp = next_dp, dp

  print(dp[-1])