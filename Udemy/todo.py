while True:
  user_action = input("Type add, show,edit,complete or exit :")
  user_action = user_action.strip()
  match user_action:
    case 'add':
      todo = input("Enter a todo: ")+"\n"
      
      with open('todo.txt','r') as file:
        todos = file.readlines()

      todos.append(todo)

      with open('todo.txt','w') as file:
        file.writelines(todos)
    case 'show':
      with open('todo.txt','r') as file:
        todos = file.readlines()
      
      for index,item in enumerate(todos):
        item = item.strip('\n')
        print(index+1,")",item)
    case 'edit':
      num = int(input("Enter the index of item: "))
      new = input("Enter new Todo:")
      
      with open('todo.txt','r') as file:
        todos = file.readlines()
      # print("Existing:",todos)
      todos[num-1] = new + "\n"
      # print("new todo:",todos)
      with open('todo.txt','w') as file:
        file.writelines(todos)
    case 'exit':
      break
    case 'complete':
      num = int(input("Enter the index of item completed:"))

      with open('todo.txt','r') as file:
        todos = file.readlines()
        
      todos.pop(num-1)

      with open('todo.txt','w') as file:
        file.writelines(todos)



# with "with" method if the program not run due to some error and stops midway then also the file closes. but in file.close() if file stops midway then file.stop() will not run