const apiKey = "7e9f4ded8aa00fe2afabeae09fa8bd9d"
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?units=metric&q=`
 
const searchInput = document.querySelector(".search-box input")
const searchButton = document.querySelector(".search-box button")
const weatherIcon = document.querySelector(".weather-image i")
const weather = document.querySelector(".weather")
const errorText = document.querySelector(".error")
 
async function checkWeather(city) {
  const response = await fetch(apiUrl + city + `&appid=${apiKey}`)
 
  if (response.status === 404) {
    errorText.style.display = "block"
    weather.style.display = "none"
  } else {
    const data = await response.json()
    console.log(data)
    document.querySelector(".city").innerHTML = data.name
    document.querySelector(".temp").innerHTML =
      Math.round(data.main.temp) + "&#8451"
 
    document.querySelector(".humidity").innerHTML = data.main.humidity + "%"
    document.querySelector(".wind").innerHTML = data.wind.speed + "km/h"
 
    weather.style.display = "block"
    errorText.style.display = "none"
  }
}
 
searchButton.addEventListener("click", () => {
  checkWeather(searchInput.value)
  searchInput.value = ""
})
 
searchInput.addEventListener("keydown", (event) => {
  if (event.keyCode === 13) {
    checkWeather(searchInput.value)
    searchInput.value = ""
  }
})

