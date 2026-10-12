const slider_input = document.getElementById("time_slider")
const slider_output_p = document.getElementById("output_text")
const slider_date_select = document.getElementById("date_select")


slider_output_p.textContent = slider_input.value;
slider_input.addEventListener("input", (selected_value) => {

    const inputValue = selected_value.target.value;
    const hours = Math.floor(inputValue/60);
    const minutes = inputValue % 60;
    const queryDate = slider_date_select.value


    //Checks if hours < 2, add an zero at start, same for minutes. So 9:00 -> 09:00 and so on
    slider_output_p.textContent = String(hours).padStart(2, "0") + ":" + String(minutes).padStart(2, "0");
})



slider_input.addEventListener("change", (send_value) => {
    const inputValue = send_value.target.value;
    const queryDate = slider_date_select.value

    const date_obj = new Date(queryDate + "T00:00")
    date_obj.setMinutes(Number(inputValue))

    update_heatmap(date_obj)
})



async function update_heatmap(date_obj) {

    //Turning the date_obj to a ISO string so python can interpret it 
    const params = new URLSearchParams({date_object: date_obj.toISOString()})
    const resp = await fetch(`/endpoints/get/intensity/heatmap/time/date?${params}`)
    const values = await resp.json()

    console.log(values)
}