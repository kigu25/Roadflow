const graph_render_box = document.getElementById("graph_render_box");
let chart;

async function render_graph(camera, date)
{
    if(chart){
        chart.destroy()
    }

    graph_render_box.style.display = "block";

    const { hourList, detectionList } = await detections_hour_by_date(camera, date)

    var options = {
    chart: {
        type: 'bar'
    },
    series: [{
        name: 'Detections',
        data: detectionList
    }],
    xaxis: {
        categories: hourList
    }
    }
    chart = new ApexCharts(document.querySelector('#chart'), options)
    chart.render()
}



async function detections_hour_by_date(camera, date)
{
    const parameters = new URLSearchParams({camera_name: camera.camera_name, date: date})
    const response1 = await fetch(`/endpoints/get/nrdetections/per/hour/bydate?${parameters}`)
    const hours_detections = await response1.json()
    console.log(hours_detections)
    const hourList = []
    const detectionList = []

    for(const data of hours_detections)
    {
        hourList.push(data.photo_hour)
        detectionList.push(data.avg_vehicles)
    }
    
    return { hourList, detectionList }
}   