const map = L.map('leaf_map').setView([56.68, 12.87], 8);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);


async function loadCameras()
{
    const response = await fetch('/endpoints/get/cameras');
    const cameras = await response.json();
    
    return cameras;
}

async function putCamerasMap()
{   
    try {
        const allCameras = await loadCameras();
        for(const camera of allCameras)
        {
            L.marker([camera.latitude, camera.longitude])
                .addTo(map)
                .bindPopup(camera.camera_name);
            console.log(camera.camera_name);
        }
    } catch (errorMsg){
        console.error("ERROR. Could not get cameras. code:", errorMsg);
    }
}

putCamerasMap();