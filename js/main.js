$(function () {
if (geoPosition.init()) {
    geoPosition.getCurrentPosition(
      success_callback,
      error_callback,
      {
        enableHighAccuracy:true
      });
  }
  else
  {
    // Cannot use geoposition, Pop up a warning/error toast, maybe allow map/stop browsing as a fallback
    
  }
  
  // p : geolocation object
  function success_callback(p){
        // p.latitude : latitude value
        // p.longitude : longitude value
        $.get('/find/nearest', {position: JSON.stringify(p)}, displayNearest);
    }

    function error_callback(p){
        // p.message : error message
    }  
});

function displayNearest(data) {
  // Zoom to the current position, or nearest bus stop on the map,
  // Highlight the nearby bus stops in the list, provide basic info on them
}