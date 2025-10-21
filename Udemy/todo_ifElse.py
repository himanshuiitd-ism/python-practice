from jarvis_overlay import show_overlay_message

while True:
  user_action = input("Type add, show,edit,complete or exit :")
  user_action = user_action.strip()
  
  if user_action.startswith('add'):
    todo = user_action[4:] + '\n'
    with open('todo.txt','r') as file:
      todos = file.readlines()
      
    todos.append(todo)
    
    with open('todo.txt','w') as file:
      file.writelines(todos)
  elif user_action.startswith('show'):
    with open('todo.txt','r') as file:
      todos = file.readlines()
    
    for index,item in enumerate(todos):
      item = item.strip('\n')
      print(index+1,")",item)
      show_overlay_message(item)
      # show_overlay_message("This is a test")
  elif user_action.startswith('edit'):
    num = int(input("Enter the index of item: "))
    new = input("Enter new Todo:")
    
    with open('todo.txt','r') as file:
      todos = file.readlines()
    # print("Existing:",todos)
    todos[num-1] = new + "\n"
    # print("new todo:",todos)
    with open('todo.txt','w') as file:
      file.writelines(todos)
  elif user_action.startswith('exit'):
    break
  elif user_action.startswith('complete'):
    num = int(input("Enter the index of item completed:"))

    with open('todo.txt','r') as file:
      todos = file.readlines()
      
    todos.pop(num-1)

    with open('todo.txt','w') as file:
      file.writelines(todos)



# in try except if there is syntax error in try block then it doesn't goes to except block bcoz try except check for exception and not the syntax error