"""
یه کلاس به اسم ZigZag پیاده‌سازی کن که دو لیست عددی رو به‌صورت زیگ‌زاگ پیمایش کنه.
این کلاس باید متدهایی داشته باشه که مقدار بعدی رو برگردونه و بررسی کنه آیا هنوز عددی باقی مونده یا نه.
 اگر یکی از لیست‌ها زودتر تموم شد، مقادیر باقی‌مونده‌ی لیست دیگه رو ادامه بده.

"""
# [1,3,5,7,9]  [2,4,6,8,10]  ==> 1  2  3  4  5  6  7  8  9  10


class ZigZag:
    def __init__(self, l1, l2):
        self.queue = [l1, l2]

    def next(self):
        v = self.queue.pop(0)
        r = v.pop(0)
        if v:
            self.queue.append(v)
        return r

    def has_next(self):
        if self.queue:
            return True
        return False


z = ZigZag([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
while z.has_next():
    print(z.next(), end=' ')