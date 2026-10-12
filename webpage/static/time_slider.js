const input = document.getElementById("time_slider")
const output_p = document.getElementById("slider_output")


output_p.textContent = input.value;
input.addEventListener("input", (selected_value) => {

    const inputValue = selected_value.target.value;
    const hours = Math.floor(inputValue/60);
    const minutes = inputValue % 60;

    //Checks if hours < 2, add an zero at start, same for minutes. So 9:00 -> 09:00 and so on
    output_p.textContent = String(hours).padStart(2, "0") + ":" + String(minutes).padStart(2, "0");
})