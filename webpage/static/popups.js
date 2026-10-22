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
            <a href='/endpoints/get/latest/imge/timeframe?${params}' target='_blank' rel='noopener'>
                <img src='/endpoints/get/latest/imge/timeframe?${params}' class="popup-img">
            </a>`
        )
}


async function fill_popups(camera, popupElement)
{
    const params = new URLSearchParams({camera_name: camera.camera_name, date_object: current_time_window.toISOString()});

    const [data_gap, all_detections] = await Promise.all([
        check_data_gap_timewindow(params),
        get_all_detections_for_popup(params)
    ]);

    const gapElement = popupElement?.querySelector(".data_gap_popup");
    if(gapElement && data_gap != null){
        gapElement.textContent = `There is a data-gap in this time-window. This means that data is partly missing for this time-window.`;
    }

     const allDetectionsElement = popupElement?.querySelector(".all_detections_popup");
     if(allDetectionsElement && all_detections != null)
     {
        allDetectionsElement.textContent = `Vehicles in selected time-window: ${all_detections.detected_vehicles}`
     }
}

async function check_data_gap_timewindow(params){
    
    const res = await fetch(`/endpoints/get/datagaps/time/date?${params}`)
    if(!res.ok)
    {
        return null;
    }
    const data_gap_dict = await res.json()
    return data_gap_dict
}

async function get_all_detections_for_popup(params)
{
    const response = await fetch(`/endpoints/get/all/detections/camera/time?${params}`)
    if(!response.ok)
    {
        return null;
    }
    const all_detections = await response.json()
    return all_detections
}