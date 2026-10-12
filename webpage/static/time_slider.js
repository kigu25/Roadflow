const input = document.getElementById("time_slider")
const output_p = document.getElementById("slider_output")


output_p.textContent = input.value;
input.addEventListener("input", (selected_value) => {

    const inputValue = selected_value.target.value;
    const hours = Math.floor(inputValue/60);
    const minutes = inputValue % 60;

    output_p.textContent = String(hours).padStart(2, "0") + ":" + String(minutes).padStart(2, "0");
})