const graph_render_box = document.getElementById("graph_render_box");
let chart;

async function render_graph(camera, date)
{
    if(chart){
        chart.destroy()
    }

    graph_render_box.style.display = "block";

    const { hourList, detectionList } = await detections_hour_by_date(camera, date)

    const options = {
    colors: ['#d64533'],
    dataLabels: { enabled: false },
    grid: {
        borderColor: '#444'
    },
    plotOptions: {
        bar: {borderRadius: 4, columnWidth: '60%'}
    },

    chart: {
        type: 'bar',
        foreColor: "#e6e5e4",
        height: "500",
        toolbar: {show:false}
        
    },
    series: [{
        name: 'Vehicles in image (average)',
        data: detectionList
    }],
    xaxis: {
        categories: hourList,
        title: { text: "Hour", style: {fontSize: '15px'} }
    },
    yaxis: {
        title: { text: "Vehicles in image (average)", style: {fontSize: '15px'} }
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