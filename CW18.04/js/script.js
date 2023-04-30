const form=document.querySelector('#form');
const input=document.querySelector('#input');
const todosUl=document.querySelector('#ul');
const todoes=JSON.parse(localStorage.getItem('toDoes'))
if (todoes){
    todoes.forEach(todo =>{
        AddToDo(todo)
        
    })
}

form.addEventListener('submit', (e)=>{
    e.preventDefault();
    AddToDo();

})

function AddToDo (todo) {
    let todoText = input.value
    if (todo)  {
        todoText = todo.text
    }
    if (todoText) {
        const todoEl=document.createElement("li");
        if (todo&&todo.completed){
            todoEl.createList.toggle("completed")
        }
        todoEl.innerText= todoText
        todoEl.addEventListener("click", (e)=>{
            e.preventDefault()
            todoEl.remove()
            UpdateLs()
        
        })
        todoEl.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            todoEl.remove();

            UpdateLs();
        });

        todosUl.appendChild(todoEl);
        input.value = '';

        UpdateLs();
    }
}

function UpdateLs (){
    const todoEl=document.querySelectorAll('li');
    const todoes=[]
    todoEl.forEach(X=>{
        todoes.push({
            text: X.innerText, 
            completed: X.classList.contains("completed")
        })
    })
    localStorage.setItem("toDoes", JSON.stringify(todoes))
}