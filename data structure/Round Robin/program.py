class TaskNode:
    """يمثل مهمة داخل الطابور"""
    def __init__(self, task_value, burst_time):
        self.task_value = task_value  # قيمة المهمة المدخلة
        self.original_burst_time = burst_time  # الوقت الأصلي المطلوب لتنفيذ المهمة
        self.remaining_time = burst_time  # الوقت المتبقي لإنهاء المهمة
        self.waiting_time = 0  # الوقت الذي انتظرته المهمة داخل الطابور
        self.execution_time = 0  # الوقت الفعلي المستهلك لتنفيذ المهمة
        self.start_time = None  # وقت بدء التنفيذ الأول
        self.next = None  # الإشارة إلى المهمة التالية في الطابور


class TaskQueue:
    """يمثل الطابور باستخدام قائمة متصلة"""

    def __init__(self):
        self.front = None  # أول عنصر في الطابور
        self.rear = None  # آخر عنصر في الطابور
        self.size = 0  # عدد المهام داخل الطابور

    def enqueue(self, task_value, burst_time):
        """إضافة مهمة إلى الطابور"""
        new_task = TaskNode(task_value, burst_time)
        if self.rear is None:  # إذا كان الطابور فارغًا
            self.front = self.rear = new_task
        else:
            self.rear.next = new_task
            self.rear = new_task
        self.size += 1

    def dequeue(self):
        """إزالة أول مهمة في الطابور"""
        if self.front is None:
            return None
        temp = self.front  # حفظ العقدة الأولى
        self.front = self.front.next  # تحديث أول عنصر
        if self.front is None:
            self.rear = None  # إذا أصبح الطابور فارغًا
        self.size -= 1
        return temp

    def is_empty(self):
        """التحقق مما إذا كان الطابور فارغًا"""
        return self.front is None

    def re_enqueue(self, task):
        """إعادة إدراج المهمة في نهاية الطابور إذا لم تكتمل"""
        if self.rear is None:
            self.front = self.rear = task
        else:
            self.rear.next = task
            self.rear = task
        task.next = None  # التأكد من أن المهمة الأخيرة لا تشير إلى أي شيء
        self.size += 1


def determine_burst_time(value):
    """تحديد وقت التنفيذ بناءً على قيمة المهمة"""
    if 1 <= value <= 5:
        return 5
    elif 6 <= value <= 10:
        return 2
    elif 11 <= value <= 20:
        return 7
    elif 21 <= value <= 30:
        return 10
    else:
        return 15


def round_robin_scheduler(task_queue, time_quantum):
    """تنفيذ المهام باستخدام خوارزمية Round Robin"""
    total_time = 0  # الوقت الإجمالي المستهلك

    while not task_queue.is_empty():
        task = task_queue.dequeue()  # أخذ أول مهمة من الطابور
        
        if task.start_time is None:
            task.start_time = total_time  # تسجيل وقت بدء التنفيذ

        # *تنفيذ المهمة لمدة time_quantum*
        execution_time = min(time_quantum, task.remaining_time)  # تنفيذ الجزء المتاح
        total_time += execution_time
        task.execution_time += execution_time
        task.remaining_time -= execution_time

        print(f"\n🔹 Executing task with value: {task.task_value} for {time_quantum} seconds...")

        if task.remaining_time <= 0:
            task.waiting_time = total_time - task.start_time - task.original_burst_time
            #task.waiting_time = total_time  - task.original_burst_time
            print(f"✅ Task with value '{task.task_value}' completed! Took: {task.execution_time} seconds. Waiting time: {task.waiting_time} seconds.")
        else:
            task_queue.re_enqueue(task)  # إرجاع المهمة إلى الطابور لإكمال تنفيذها لاحقًا


def get_tasks_from_user():
    """أخذ المدخلات من المستخدم وتخزينها في الطابور"""
    task_queue = TaskQueue()
    num_tasks = int(input("🔹 Enter the number of tasks (numbers to be entered): "))

    for i in range(num_tasks):
        task_value = int(input(f"🔹 Enter task number {i+1}: "))  # المستخدم يدخل الرقم مباشرة
        burst_time = determine_burst_time(task_value)
        task_queue.enqueue(task_value, burst_time)

    return task_queue


if __name__ == "__main__":
    time_quantum = 4
    print(f"\n🔹 Time quantum is set to: {time_quantum} seconds\n")

    task_queue = get_tasks_from_user()
    print("\n🚀 Starting Round Robin Scheduling...\n")
    
    round_robin_scheduler(task_queue, time_quantum)
    
    print("\n✅ All tasks are completed!")