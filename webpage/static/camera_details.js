const camera_name_h2 = document.getElementById("camera_name");
const camera_latitude_p = document.getElementById("latitude");
const camera_longitude_p = document.getElementById("longitude")
const camera_trafikverket_id_p = document.getElementById("trafikverket_id")
const camera_info_box_div = document.getElementById("camera_info_box");

async function showCameraDetails(camera_name)
{
    const response = await fetch(`/endpoints/get/camera/details?camera_name=${encodeURIComponent(camera_name)}`);
    const camera_data = await response.json();
    
    camera_info_box_div.style.display = "block";
    camera_name_h2.textContent = camera_data.camera_name;
    camera_trafikverket_id_p.textContent = `TrafikverketID: ${camera_data.camera_id}`;
    camera_latitude_p.textContent = `Latitude: ${camera_data.latitude}`;
    camera_longitude_p.textContent = `Longitude: ${camera_data.longitude}`;
}