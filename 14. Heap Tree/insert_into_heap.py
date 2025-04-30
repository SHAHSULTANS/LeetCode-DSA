
#Min Heap
def insert(heap,value):
    heap.append(value)
    current_index=len(heap)-1
    
    while current_index>0:
        parent_index=(current_index-1)//2
        
        if heap[current_index]<heap[parent_index]:
            heap[current_index],heap[parent_index]=heap[parent_index],heap[current_index]
        else:
            break
        current_index=parent_index




min_heap = []
values = [7, 3, 10, 1, 5, 8,-5]

for val in values:
    insert(min_heap,val)
    print(f"Heap after inserting {val}: {min_heap}")
    
    
print("")
print(min_heap)
    
    
