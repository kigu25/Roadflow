const slider_input = document.getElementById("time_slider")
const slider_output_p = document.getElementById("output_text")
const date_choice = document.getElementById("date_select")


slider_output_p.textContent = slider_input.value;
slider_input.addEventListener("input", (selected_value) => {

    const inputValue = selected_value.target.value;
    const hours = Math.floor(inputValue/60);
    const minutes = inputValue % 60;
    const queryDate = date_choice.value


    //Checks if hours < 2, add an zero at start, same for minutes. So 9:00 -> 09:00 and so on
    slider_output_p.textContent = String(hours).padStart(2, "0") + ":" + String(minutes).padStart(2, "0");
})