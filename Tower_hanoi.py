#Recursion ,  Stack

# def Tower_hanoi(disk, source, helper, target):
#     if disk == 1:
#         print(f"Move disk from {source} to {target}")
#         return
#     Tower_hanoi(disk-1,source,target,helper)
#     print(f"Move disk from {source} to {target}")
#     Tower_hanoi(disk-1,helper, source, target)

def tower_hanoi(disk,source,helper,target):
  if disk ==1:
    print(f"Move Disk from {source} to {target}")
    return

  tower_hanoi(disk-1,source,target,helper)
  print(f"Move Disk from {source} to {target}")

  tower_hanoi(disk-1,helper,source,target)

tower_hanoi(2, 'A', 'B', 'C')
