var data;
var mapModule = (function(window,$) {

    var MAPBOX_ACCESS_TOKEN = resourceTokensModule.MAPBOX_ACCESS_TOKEN;
    var MAPBOX_MAP_STYLE_ID = 'lightfox.1n10e3dp';
    var MAP_CONTAINER_ELEMENT_ID = 'map';
    // var ICON_RULES = configModule.rules
    // var DEFAULT_ICON = './gfx/img_markers_walking.png'

    var SEARCH_MARKER_GEOJSON = {
        type: 'Feature',
        geometry: { type: 'Point' },
        properties: { 'marker-size': 'large' }
    };

    var METERS_PER_FOOT = 0.3048;

    var featureGroup = L.featureGroup();

    var SHAPE_STYLE_SETTINGS = {
        color: '#0033ff',
        fillColor: '#0033ff',
        weight: 5,
        fillOpacity: 0.2,
        opacity: 0.5
    };

    var DRAW_CONTROL_SETTINGS = {
        draw: {
            polyline: false,
            polygon: { shapeOptions: SHAPE_STYLE_SETTINGS },
            rectangle: { shapeOptions: SHAPE_STYLE_SETTINGS },
            circle: { shapeOptions: SHAPE_STYLE_SETTINGS }
        },
        edit: {
            featureGroup: featureGroup,
        }
    };

    var map;

    function _init() {
        L.mapbox.accessToken = MAPBOX_ACCESS_TOKEN;
        map = L.map(MAP_CONTAINER_ELEMENT_ID).setView([37.76, -122.407], 12);
        L.mapbox.tileLayer('bobbysud.i2pfp2lb', {detectRetina: true}).addTo(map);

        featureGroup.addTo(map);

        var drawControl = new L.Control.Draw(DRAW_CONTROL_SETTINGS).addTo(map);

        map.on('draw:created', function(e) {

            // Each time a feaute is created, it's added to the over arching feature group
            featureGroup.addLayer(e.layer);
        });
    }

    function saveConfirm(data) {
        console.log("sent to server");
        $('#name').val("");
        featureGroup.clearLayers();
    }

    function saveGeometery(evt) {
        evt.preventDefault();

        data = featureGroup.toGeoJSON();

        var name = $('#name').val()
        var shape = data.features[0].geometry.type;
        var lat = JSON.stringify(data.features[0].geometry.coordinates[0]);
        var long = JSON.stringify(data.features[0].geometry.coordinates[1]);

        var convertedData = {
            "name": name,
            "shape": shape,
            "lat": lat,
            "long": long
        }


        $.get('/save_geometery.json', 
             convertedData, 
             saveConfirm);
    }

    $('#export').on('submit', saveGeometery);

    function _convertFromFeetToMeters(feet) {
        return feet * METERS_PER_FOOT;
    }

    function _convertFromMetersToFeet(meters) {
        return meters / METERS_PER_FOOT;
    }

    return {
        init: _init
    };

})(window, jQuery);
