const map = L.map('leaf_map').setView([56.68, 12.87], 8);

L.tileLayer('https://basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}.png?key=cb1_46bu_1_51611b2dfbf363bc33bc24dd',  {
    subdomains: 'abcd',
    maxZoom: 16,
    attribution: '© CARTO basemaps'
}).addTo(map);


async function loadCameras()
{
    const response = await fetch('/endpoints/get/all/camera/data');
    const cameras = await response.json();
    
    return cameras;
}

async function putCamerasMap()
{   
    try {
        const allCameras = await loadCameras();
        for(const camera of allCameras)
        {
            const marker = L.marker([camera.latitude, camera.longitude])
                .addTo(map)
                .bindPopup(camera.camera_name);
            
            marker.on("click", () => {
                showCameraDetails(camera); 
                graphs_render(camera, "2026-10-06");
            });
        }
    } catch (errorMsg){
        console.error("ERROR. Could not get cameras. code:", errorMsg);
    }
}

putCamerasMap();