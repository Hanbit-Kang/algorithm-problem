# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

if __name__ == '__main__':
  # ����/��/6���� �ڷ���Ʈ ���� ... �� 8���� ���ȭ
  positions = [list(map(int, input().split())) for _ in range(2)]
  dists = [[float('inf')]*8 for _ in range(8)]    
                                            
  for n in range(2, 8, 2): # 2-3/4-5/6-7
    x1, y1, x2, y2 = map(int, input().split()) 
    positions.append([x1,y1])
    positions.append([x2,y2])

    dists[n][n+1] = 10                  
    dists[n+1][n] = 10                  
                   
  for i in range(8):
    for j in range(i, 8):
      diff = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
      
      # �ڷ���Ʈ���� ������ �� ���� ���� ����
      dists[i][j] = min(dists[i][j], diff)
      dists[j][i] = min(dists[j][i], diff)

  # �÷��̵� �ͼ�
  for k in range(8):
    for i in range(8):
      for j in range(8):
        if dists[i][j] > dists[i][k] + dists[k][j]:
          dists[i][j] = dists[i][k] + dists[k][j]
  print(dists[0][1])