const graph_render_box = document.getElementById("graph_render_box");
const graph_stats = document.getElementById("stats");

async function graphs_render(camera, date)
{
    const parameters = new URLSearchParams({camera_name: camera.camera_name, date: date})
    const response1 = await fetch(`/endpoints/get/nrdetections/per/hour/bydate?${parameters}`)
    const hours_detections = await response1.json()
    console.log(hours_detections)

    graph_render_box.style.display = "block";

}   