async function showCameraDetails(camera_name)
{
    const response = await fetch(`/endpoints/get/camera/details?camera_name=${encodeURIComponent(camera_name)}`);
    const camera_data = await response.json();
    
    console.log(camera_data['camera_name']);
}