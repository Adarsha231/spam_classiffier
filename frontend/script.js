const email = document.getElementById("email")
const checkBtn = document.getElementById("checkBtn")
const result = document.getElementById("result")


const prediction = document.querySelector(".prediction")
const probability = document.querySelector(".probability")

checkBtn.addEventListener("click", async function () {

    const emailText = email.value

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            email: emailText
        })
    })
    const data = await response.json()
    result.style.display = "block"
    prediction.textContent = data.prediction
    probability.textContent = `Spam Probability: ${data.spam_probability}%`

})

