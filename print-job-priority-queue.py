import heapq

class PrintJob:
    def __init__(self, document, employee_name, seniority):
        self.document = document
        self.employee_name = employee_name
        self.seniority = seniority

    def __lt__(self, other):
        # This is reversed to create a max heap instead of a min heap
        return self.seniority > other.seniority

class PrintQueue:
    def __init__(self):
        self.queue = []

    def add_print_job(self, document, employee_name, seniority):
        job = PrintJob(document, employee_name, seniority)
        heapq.heappush(self.queue, job)

    def print_next_job(self):
        if not self.is_empty():
            job = heapq.heappop(self.queue)
            print(f"Printing document: {job.document} for {job.employee_name} (Seniority: {job.seniority})")
        else:
            print("No jobs in the queue.")

    def is_empty(self):
        return len(self.queue) == 0

    def queue_size(self):
        return len(self.queue)

# Example usage
print_queue = PrintQueue()

# Add print jobs
print_queue.add_print_job("Budget Report", "John (CEO)", 10)
print_queue.add_print_job("Meeting Minutes", "Alice (Manager)", 7)
print_queue.add_print_job("Project Proposal", "Bob (Team Lead)", 5)
print_queue.add_print_job("Weekly Schedule", "Carol (Employee)", 3)

# Print jobs
print(f"Number of jobs in queue: {print_queue.queue_size()}")
while not print_queue.is_empty():
    print_queue.print_next_job()

# Add more jobs
print_queue.add_print_job("Urgent Memo", "John (CEO)", 10)
print_queue.add_print_job("Department Report", "Alice (Manager)", 7)

# Print new jobs
print(f"\nNumber of jobs in queue: {print_queue.queue_size()}")
while not print_queue.is_empty():
    print_queue.print_next_job()
