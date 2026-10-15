const slider_input = document.getElementById("time_slider")
const slider_output_p = document.getElementById("output_text")
const slider_date_select = document.getElementById("date_select")
const lowIntensity = 3.5
const mediumIntensity = 7.5


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
    update_heatmap()
})



async function update_heatmap() {
    const inputValue = slider_input.value;
    const queryDate = slider_date_select.value

    const date_obj = new Date(queryDate + "T00:00")
    date_obj.setMinutes(Number(inputValue))

    //Turning the date_obj to a ISO string so python can interpret it 
    const params = new URLSearchParams({date_object: date_obj.toISOString()})
    const resp = await fetch(`/endpoints/get/intensity/heatmap/time/date?${params}`)
    const cameraValuesIntensity = await resp.json()

    console.log(cameraValuesIntensity)

    intensityRulesMapCircles(cameraValuesIntensity, circle_marker_dict);
}


function intensityRulesMapCircles(cameraValues, circle_marker_dict)
{

    for(const camera of cameraValues)
    {
        if(camera.avg_vehicles == null)
        {
            //TODO: This should change the camera-icon to show not availabel aswell, not only radius
            circle_marker_dict[camera.camera_id].setStyle({ fillOpacity: 0.8, fillColor : "grey" });
        }

        else if(camera.avg_vehicles <= lowIntensity){
            circle_marker_dict[camera.camera_id].setStyle({ fillOpacity: 0.6, fillColor : "#22C55E" });
        }

        else if(camera.avg_vehicles <= mediumIntensity)
        {
            circle_marker_dict[camera.camera_id].setStyle({ fillOpacity: 0.6, fillColor : "#F59E0B" });
        }

        else{
            circle_marker_dict[camera.camera_id].setStyle({ fillOpacity: 0.6, fillColor : "#EF4444" });
        }
    }
}