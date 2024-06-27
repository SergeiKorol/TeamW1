from ToDoList import ToDoList


api = ToDoList('https://todo-app-sky.herokuapp.com')


#  создание задачи, удаление и запрос удаленной задачи
def test_delete_Ann_task():
    new_task = api.create_task('Task by Ann to be deleted')
    taskid = new_task.json()['id']
    list_of_tasks1 = api.get_tasks()
    result = api.delete_task(taskid)
    list_of_tasks2 = api.get_tasks()
    get_dell = api.get_task_by_id(taskid)
    # a = get_dell.json()
    assert result.status_code == 200
    assert len(list_of_tasks2) == len(list_of_tasks1) - 1
    assert get_dell.status_code == 404
    #assert get_dell.json() is None