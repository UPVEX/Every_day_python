# کد زیر الگوریتم حل برج هانوی هستش که از ورودی یه عدد میگیره و مراحل طی کردن برج رو میگه و تعداد دفعات تکرار رو هم نمایش میده



def tower_of_hanoi(n, source, target, auxiliary, step_count):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        step_count = tower_of_hanoi(n-1, source, auxiliary, target, step_count)
        
        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        step_count += 1
        
        # Move the n-1 disks from auxiliary to target peg
        step_count = tower_of_hanoi(n-1, auxiliary, target, source, step_count)
    
    return step_count

def tower_hanoi_steps(n):
    print(f"Solving Tower of Hanoi for {n} disks:")
    steps = tower_of_hanoi(n, 'A', 'C', 'B', 0)
    print(f"Total steps: {steps}")

# Get input from user
num_disks = int(input("Enter the number of disks: "))
tower_hanoi_steps(num_disks)

