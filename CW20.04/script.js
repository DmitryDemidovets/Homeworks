const input = document.querySelector('#textfield')
const btn = document.querySelector('#form__btn')
const output = document.querySelector('#output')

console.log(input.textContent)

function clickHandler() {
    localStorage.setItem("data", input.value)
}

btn.addEventListener('click', () => clickHandler())

const lsData = localStorage.getItem("data");
output.innerText = lsData

