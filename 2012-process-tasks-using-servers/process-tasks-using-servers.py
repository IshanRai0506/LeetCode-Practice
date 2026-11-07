import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # free_servers stores: (weight, index)
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        
        # busy_servers stores: (free_time, weight, index)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            # Track time: cannot process task j before second j
            curr_time = max(curr_time, j)
            
            # If all servers are busy, fast-forward time to the next available server
            if not free_servers:
                curr_time = busy_servers[0][0]
            
            # Release all servers whose task completion time is <= curr_time
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            
            # Assign task to the available server with (smallest weight, smallest index)
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            
            # Mark server as busy until curr_time + task_time
            heapq.heappush(busy_servers, (curr_time + task_time, weight, index))
            
        return ans