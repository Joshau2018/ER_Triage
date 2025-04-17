import heapq

class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # higher = more urgent

    def __lt__(self, other):
        # Invert comparison to make heapq act as a max-heap
        return self.priority > other.priority

    def __str__(self):
        return f"{self.name} ({self.priority})"

class TriageQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, patient):
        # insert the patient into the queue
        if self.is_empty:
            heapq.heappush(self.heap, patient)
        else:
            heapq.heappush(self.heap, patient)
            self.max_heap_percolate_up(len(self.heap) - 1)

        # Call visualize to display and log the entire queue
        self.visualize

    def dequeue(self):
        log_file = open("/home/johsua/Documents/ER_Triage/patients.txt", "l")
        # if the queue is empty display "No patients in queue"
        if self.is_empty:
            print("No patient in queue")

        # Display and log the patient treated and their priority
        treated_patient = heapq.heappop(self.heap)
        print(treated_patient.__str__()) 
        log_file.write(treated_patient.__str__())
        log_file.close()
        self.min_heap_percolate_up(0)

        # Call visualize to display and log the entire queue
        self.visualize
        # Return the dequeued patient
        return treated_patient
    
    def max_heap_percolate_up(self, node_index):
        while node_index > 0:
            parent_index = (node_index - 1) / 2
            if not self.heap[node_index].__lt__(): # idk I got confused with this logic
                return
            else:
                self.heap[node_index], self.heap[parent_index] = self.heap[parent_index], self.heap[node_index]
                node_index = parent_index
    
    def min_heap_percolate_up(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap[node_index]
        while child_index < len(self.heap):
            if child_index + 1 < len(self.heap):
                if self.heap[child_index].__lt__(child_index + 1):
                    max_val = self.heap[child_index]
                    max_index = child_index
                else:
                    max_val = self.heap[child_index + 1]
                    max_index = child_index + 1
                if max_val == value:
                    return
                else:
                    self.heap[node_index], self.heap[max_index] = self.heap[max_index], self.heap[node_index]
            else:
                return


    def peek(self):
        # Return the patient at the root or None if the heap is empty
        if self.is_empty():
            return
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0
        

    def visualize(self):
        # Print the contents of the current priority queue
        # to both the display and the log file
        
        
        log_file = open("/home/johsua/Documents/ER_Triage/JoshuaKlarich_LogFile.txt", "l")
        log_file.write(self.heap)
        log_file.close()
        print(self.heap)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    name, priority = parts[0], int(parts[1])
                    self.enqueue(Patient(name, priority))

# Example usage
if __name__ == "__main__":
    triage = TriageQueue()
    triage.load_from_file("/home/johsua/Documents/ER_Triage/patients.txt")
    

    while not triage.is_empty():
        print(triage.peek().name)
        triage.dequeue()
