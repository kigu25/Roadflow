const camera_name_h2 = document.getElementById("camera_name");
const camera_latitude_p = document.getElementById("latitude");
const camera_longitude_p = document.getElementById("longitude")
const camera_trafikverket_id_p = document.getElementById("trafikverket_id")
const camera_info_box_div = document.getElementById("camera_info_box");
const img_box = document.getElementById("latest_camera_img")
const avg_p = document.getElementById("avg_vehicles")


async function showCameraDetails(camera)
{
    const resp = await fetch(`/endpoints/get/avg/detections/day?camera_name=${encodeURIComponent(camera.camera_name)}`)
    const avg_detections = await resp.json()

    camera_info_box_div.style.display = "block";
    camera_name_h2.textContent = camera.camera_name;
    camera_trafikverket_id_p.textContent = `TrafikverketID: ${camera.trafikverket_id}`;
    camera_latitude_p.textContent = `Latitude: ${camera.latitude}`;
    camera_longitude_p.textContent = `Longitude: ${camera.longitude}`;
    avg_p.textContent = `Average detections per day: ${avg_detections.avg_detections_day}`
    img_box.src = `/endpoints/get/latest/img?camera_name=${encodeURIComponent(camera.camera_name)}`

}