function unavailable_popup(camera, marker)
{
    marker.setPopupContent(`
        <h4>${camera.camera_name}</h4>
        <h3 class="data_gap_popup"></h3>
        <p> Camera was unavailable during selected time-window.</p>`)
}

function available_popup(camera, marker, date_obj)
{
    const params = new URLSearchParams({camera_name: camera.camera_name, date_object: date_obj.toISOString()})

    marker.setPopupContent(`
            <h3>${camera.camera_name}</h3>
            <p>AVG vehicles in time-window: ${camera.avg_vehicles}</p>
            <p class='all_detections_popup'></p>
            <h4 class="data_gap_popup"></h4>
            <img src='/endpoints/get/latest/imge/timeframe?${params}' class="popup-img">`
        )
}

async function check_data_gap_timewindow(params){
    
    const res = await fetch(`/endpoints/get/datagaps/time/date?${params}`)
    const data_gap_dict = await res.json()
    return data_gap_dict
}

async function get_popup_data_for_camera(params)
{
    const response = await fetch(`/endpoints/get/all/detections/camera/time?${params}`)
    const all_detections = await response.json()
    return all_detections
}