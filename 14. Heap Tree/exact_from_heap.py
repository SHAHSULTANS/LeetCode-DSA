
#Min Heap
from turtle import right


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

def heapify_down(heap,index):
    size=len(heap)
    smallest=index
    left_child=2*index+1
    right_child=2*index+2
    
    if left_child<size and heap[left_child]<heap[smallest]:
        smallest=left_child
    if right_child<size and heap[right_child]<heap[smallest]:
        smallest=right_child
    
    if smallest!=index:    
        heap[index],heap[smallest]=heap[smallest],heap[index]
        heapify_down(heap,smallest)
    



def extract_min(heap):
    if len(heap)==0:
        return None
    
    min_value=heap[0]
    heap[0]=heap[-1]
    heap.pop()  
    heapify_down(heap,0)
    return min_value


min_heap = []
values = [7, 3, 10, 1, 5, 8,-5]

for val in values:
    insert(min_heap,val)
    print(f"Heap after inserting {val}: {min_heap}")
    
    
print("")
print(min_heap)

print("")
print("Extracting min values:")
for _ in range(len(min_heap)):
    min_value=extract_min(min_heap)
    print(f"Extracted min value: {min_value}")
    # print(f"Heap after extracting min value: {min_heap}")
    
    
