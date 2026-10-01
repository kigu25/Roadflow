const map = L.map('leaf_map').setView([56.68, 12.87], 8);

L.tileLayer('https://basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png?key=cb1_46bu_1_51611b2dfbf363bc33bc24dd',  {
    subdomains: 'abcd',
    maxZoom: 16,
    attribution: '© CARTO basemaps'
}).addTo(map);


async function loadCameras()
{
    const response = await fetch('/endpoints/get/camera/coords');
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