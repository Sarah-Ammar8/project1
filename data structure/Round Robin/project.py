#  تعريف كلاس يمثل العقدة في الطابور (المهمة)
class TaskNode:
    def __init__(self, task_value, burst_time):
        self.task_value = task_value  # القيمة المدخلة للمهمة
        self.original_burst_time = burst_time  # الزمن الأصلي المطلوب لتنفيذ المهمة
        self.remaining_time = burst_time  # الزمن المتبقي للتنفيذ
        self.execution_time = 0  # الوقت الفعلي الذي استهلكته المهمة
        self.start_time = None  # وقت بدء التنفيذ
        self.next = None  # مؤشر إلى العقدة التالية

#  إنشاء كلاس يمثل الطابور باستخدام قائمة متصلة
class TaskQueue:
    def __init__(self):
        self.front = None  # أول عنصر في الطابور
        self.rear = None  # آخر عنصر في الطابور
        self.size = 0  # عدد المهام

    # 🔹 دالة لإضافة مهمة إلى الطابور (enqueue)
    def enqueue(self, task_value, burst_time):
        new_task = TaskNode(task_value, burst_time)
        if self.rear is None:  # إذا كان الطابور فارغًا
            self.front = self.rear = new_task
        else:
            self.rear.next = new_task  # ربط العقدة الجديدة بآخر عقدة
            self.rear = new_task  # تحديث المؤشر إلى آخر عقدة
        self.size += 1

    # 🔹 دالة لإزالة أول مهمة من الطابور (dequeue)
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front  # الحصول على أول عقدة في الطابور
        self.front = self.front.next  # تحديث أول عنصر ليكون التالي
        if self.front is None:  # إذا أصبح الطابور فارغًا
            self.rear = None
        self.size -= 1
        return temp  # إرجاع العقدة المحذوفة

    # 🔹 دالة للتحقق مما إذا كان الطابور فارغًا
    def is_empty(self):
        return self.front is None

    # 🔹 دالة لإعادة إدخال المهمة إلى نهاية الطابور
    def re_enqueue(self, task):
        if self.rear is None:
            self.front = self.rear = task
        else:
            self.rear.next = task
            self.rear = task
        task.next = None  # التأكد من أن العقدة الأخيرة لا تشير إلى عقدة أخرى
        self.size += 1

#  دالة لتحديد وقت التنفيذ تلقائيًا بناءً على الإدخال
def determine_burst_time(value):
    if 1 <= value <= 5:
        return 5
    elif 6 <= value <= 10:
        return 6
    elif 11 <= value <= 20:
        return 7
    elif 21 <= value <= 30:
        return 10
    else:
        return 15

#  دالة تنفيذ Round Robin بحيث تأخذ كل مهمة الوقت المحدد بالكامل
def round_robin_scheduler(task_queue, time_quantum):
    total_time = 0  # إجمالي وقت التنفيذ

    while not task_queue.is_empty():
        task = task_queue.dequeue()  # أخذ أول مهمة في الطابور

        # تعيين وقت البدء لأول مرة
        if task.start_time is None:
            task.start_time = total_time

        # تنفيذ المهمة لمدة time_quantum بالكامل حتى لو كانت تحتاج أقل
        print(f"\n🔹 Executing task with value: {task.task_value} for {time_quantum} seconds...")
        total_time += time_quantum  # تحديث إجمالي الوقت
        task.execution_time += time_quantum  # تسجيل الوقت المستهلك بالكامل

        # تقليل الزمن المتبقي للمهمة (قد يصبح سالبًا ولكن لا يؤثر على الحسابات)
        task.remaining_time -= time_quantum

        if task.remaining_time <= 0:
            #task.waiting_time = total_time - task.start_time - task.original_burst_time
            print(f"✅ Task with value '{task.task_value}' completed! Took: {task.execution_time} seconds.")
        else:
            # إذا لم تنتهِ المهمة، يتم إعادتها إلى نهاية الطابور
            task_queue.re_enqueue(task)

#  دالة لإدخال الأرقام من المستخدم مباشرة
def get_tasks_from_user():
    task_queue = TaskQueue()
    num_tasks = int(input("🔹 Enter the number of tasks (numbers to be entered): "))

    for i in range(num_tasks):
        task_value = int(input(f"🔹 Enter task number {i+1}: "))  # المستخدم يدخل الرقم مباشرة
        burst_time = determine_burst_time(task_value)  # تعيين زمن التنفيذ بناءً على الرقم المدخل
        task_queue.enqueue(task_value, burst_time)

    return task_queue

#  تشغيل الجدولة باستخدام Round Robin
if __name__ == "__main__":
    time_quantum = 4  # زمن الكمية المحدد من قبل المبرمج
    print(f"\n🔹 Time quantum is set to: {time_quantum} seconds\n")

    task_queue = get_tasks_from_user()

    print("\n🚀 Starting Round Robin Scheduling...\n")
    round_robin_scheduler(task_queue, time_quantum)
    print("\n✅ All tasks are completed!")