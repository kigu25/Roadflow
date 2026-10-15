function unavailable_popup(camera, marker)
{
    marker.setPopupContent(`<h4>${camera.camera_name}</h4><p> Camera was unavailable during selected time-window.</p>`)
}

function available_popup(camera, marker, date_obj)
{
    const params = new URLSearchParams({camera_name: camera.camera_name, date_object: date_obj.toISOString()})
    marker.setPopupContent(`<h4>${camera.camera_name}</h4>
            <p>AVG vehicles in time-window: ${camera.avg_vehicles}</p>
            <img src='/endpoints/get/latest/imge/timeframe?${params}' class="popup-img">`
        )
}