const map = L.map('leaf_map').setView([56.68, 12.87], 8);
const map_slider_date_select = document.getElementById("date_select")
const circle_marker_dict = {}


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

async function LoadCamerasAndMarkersOnMap()
{   
    try {
        const allCameras = await loadCameras();
        for(const camera of allCameras)
        {
            
            const circle_heat = L.circleMarker([camera.latitude, camera.longitude], {
                radius:25,
                color: "#d64533",
                weight: 0,
                fillColor: "#d64533",
                fillOpacity: 0
            }).addTo(map);

            const marker = L.marker([camera.latitude, camera.longitude])
                .addTo(map)
                .bindPopup(camera.camera_name);
            
            marker.on("click", () => {
                showCameraDetails(camera); 
                render_graph(camera, map_slider_date_select.value);
            });

            //Add the camera_id and the circle-object to the same dict so it can be used later to get the circle-object by camera_id.
            circle_marker_dict[camera.camera_id] = circle_heat

        }
    } catch (errorMsg){
        console.error("ERROR. Could not get cameras. code:", errorMsg);
    }
}


LoadCamerasAndMarkersOnMap();