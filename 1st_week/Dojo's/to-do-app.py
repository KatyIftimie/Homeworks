# not done

"""
listing tasks
adding a new task
marking a task as completed
archive (deleting all complete tasks)
"""
tasks = ["fefw", "fewfw", "fewf"]
# printing_tasks = ""


def listing_tasks(tasks):
    for count, item in enumerate(tasks, 1):
        printing_tasks = str(count) + "." + " [ ] " + str(item)
        print(printing_tasks)
    return main()


def adding_task(tasks):
    get_item = input("Add an item: ")
    tasks.append(get_item)
    print("Item added")
    return main()


def mark(listing_tasks,tasks):
    get_item_to_mark = int(input("Which one you want to mark as completed: "))
    
    return main()

def main():
    user_choice = input("Please specify a command [list, add, mark, archive]: ")
    user_choice = user_choice.lower()
    if user_choice == "list":
        listing_tasks(tasks)
    elif user_choice == "add":
        adding_task(tasks)
    elif user_choice == "mark":
        mark(listing_tasks, tasks)


if __name__ == "__main__":
    main()