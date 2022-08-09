# -*- coding: utf-8 -*-
import sys
import queue
input = sys.stdin.readline

# 3ȸ �̵� �� ������ ��� ��ǥ
# �����¿� / ü�� ����Ʈ / 3ĭ �����¿�
dx = [1,-1,0,0, 2,2,-2,-2,1,-1,1,-1, 3,-3,0,0]
dy = [0,0,1,-1, 1,-1,1,-1,2,2,-2,-2, 0,0,3,-3]

def f():   
  dist = [[float('inf')]*N for _ in range(N)]
  dist[0][0] = 0
  pq = queue.PriorityQueue()
  pq.put([0, 0, 0]) # dist, x, y

  # 3ĭ ���� ���ͽ�Ʈ��
  while(not pq.empty()):
    d, x, y = pq.get()
    for k in range(16):
      nx, ny = x + dx[k], y + dy[k]        

      if(0<=nx<=N-1 and 0<=ny<=N-1):        
        nd = d + 3*T + grid[nx][ny]
        if(dist[nx][ny] > nd):
          dist[nx][ny] = nd
          pq.put([nd,nx,ny])
                       
  # ������ ĭ���� 2ȸ �̳��� ���� ������ �������� �ּڰ��� ���Ѵ�.      
  return min(
    dist[-1][-1],
    dist[-2][-1] + T, dist[-1][-2],
    dist[-3][-1] + 2*T, dist[-2][-2] + 2*T, dist[-1][-3] + 2*T
  )


if __name__ == '__main__':
  N, T = map(int, input().split())
  grid = [list(map(int, input().split())) for _ in range(N)]    
                                 
  print(f())   