# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

# ���Ϸθ� �������� �� ���ù޴� Ÿ�Ե�
free = {"Mugunghwa","ITX-Saemaeul","ITX-Cheongchun"}
half = {"S-Train","V-Train"}
            
if __name__ == '__main__':
  N, R = map(int, input().split())
  names = list(map(str, input().split()))      

  # ���ڿ� ����: name_to_index["Boseong"] = 0
  name_to_index = {names[i]:i for i in range(N)}

  M = int(input())    
  target_indices = [name_to_index[name] for name in list(map(str, input().split()))]

  # �׷���ȭ
  graph = [[float('inf')]*N for _ in range(N)]
  graph_with_ticket = [[float('inf')]*N for _ in range(N)]

  K = int(input())    
  for _ in range(K):
    typee, s, e, cost = map(str, input().split())
    s_index = name_to_index[s]
    e_index = name_to_index[e]
    cost = int(cost)

    # Ƽ�� X
    graph[s_index][e_index] = min(graph[s_index][e_index], cost)
    graph[e_index][s_index] = min(graph[e_index][s_index], cost) 
        
    # Ƽ�� O
    if typee in free:
      cost = 0
    elif typee in half:
      cost /= 2
    graph_with_ticket[s_index][e_index] = min(graph_with_ticket[s_index][e_index], cost)
    graph_with_ticket[e_index][s_index] = min(graph_with_ticket[e_index][s_index], cost)
  
  # �÷��̵� �ͼ�
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if graph[i][j] > graph[i][k] + graph[k][j]:
          graph[i][j] = graph[i][k] + graph[k][j]
        if graph_with_ticket[i][j] > graph_with_ticket[i][k] + graph_with_ticket[k][j]:
          graph_with_ticket[i][j] = graph_with_ticket[i][k] + graph_with_ticket[k][j]
  
  # ���������� ����
  dist = 0
  dist_with_ticket = 0
  for i in range(M-1):
    fr, to = target_indices[i], target_indices[i+1]

    dist += graph[fr][to]  
    dist_with_ticket += graph_with_ticket[fr][to]  
  
  # ��� ��
  if dist > dist_with_ticket + R:
    print("Yes")
  else:
    print("No")