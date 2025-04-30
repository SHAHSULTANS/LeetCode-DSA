

from turtle import right


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap=[]
        
        def insert_to_max_heap(value):
            self.heap.append(value)
            current_index=len(self.heap)-1
            
            
            while current_index>0:
                parent_index=(current_index-1)//2
                
                if self.heap[parent_index]<self.heap[current_index]:
                    self.heap[current_index],self.heap[parent_index]=self.heap[parent_index],self.heap[current_index]
                    current_index=parent_index
                else:
                    break
                
        for item in nums:
            insert_to_max_heap(item)
            
            
            
            
            
            
        #________________extract from heap_____________________________
        def heapify_down(index):
            greatest_element_index=index
            left_child_index=2*index+1
            right_child_index=2*index+2
            size=len(self.heap)
            
            if left_child_index<size and self.heap[left_child_index]>self.heap[greatest_element_index]:
                greatest_element_index=left_child_index
            
            if right_child_index<size and self.heap[right_child_index]>self.heap[greatest_element_index]:
                greatest_element_index=right_child_index
                
            if greatest_element_index!=index:
                self.heap[greatest_element_index],self.heap[index]=self.heap[index],self.heap[greatest_element_index]
                heapify_down(greatest_element_index)
        
        
        def extract_max_heap():
            max_value=self.heap[0]
            self.heap[0]=self.heap[-1]
            self.heap.pop()
            heapify_down(0)
            return max_value
        
        kth_max_value=None
        for _ in range(k):
            kth_max_value=extract_max_heap()
            
        return kth_max_value
            
           
            
            
        
        # print(self.heap)
        
        