const map = L.map('leaf_map').setView([59.27, 15.21], 10);

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