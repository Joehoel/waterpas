
var count = 0;
var count2 = 0;
var verplaatsingChart;
var pointsChart;
function loop() {
    setInterval(function() {
    fetchInfo();
    }, 10 * 100); 
}

function fetchInfo() {
    var pitch = [];
    var pitchraw= [];
    var roll = [];
    var rollraw = [];
    const url =  "http://10.80.17.1/throwdata.py";
    fetch(url)        
    .then(response => response.json())
    .then(function(data) {
        for (i = 0; i < 20; i++) {
	 
            // create raw data
            pitchraw.push(data[i].pitch)
            rollraw.push(data[i].roll)

            // calc dif in movemend from last point
            if (data[i].pitch > 180) {
                pitch.push((360 - data[i].pitch))  
            } else if (data[i].pitch < 180) {
                pitch.push((0 - data[i].pitch))
            } else if (data[i].pitch == 180 ){
                pitch.push((data[i].pitch - 180))
            }

            if (data[i].roll > 180) {
                roll.push((360 - data[i].roll))    
            } else if (data[i].roll < 180) {
                roll.push((0 - data[i].roll))
            } else if (data[i].roll == 180 ){
                roll.push((data[i].roll - 180))
            }
        }
        console.log(data)
        console.log(pitchraw, rollraw)
        document.getElementById("pitch").innerHTML = "<p>"  + "pitch: " + data[19].pitch + "&deg" + "</p>"
        document.getElementById("roll").innerHTML = "<p>"  + "roll: " + data[19].roll + "&deg" + "</p>"
        draw(pitch, roll, pitchraw, rollraw)
        });
}

function draw(pitch, roll, pitchraw, rollraw) {
    if (count === 0) {
        count = 2
        console.log("draw")
        drawChartVerplaatsing(pitch, roll, document.getElementById("pitchChart").getContext('2d'))
        drawChartPoints(pitchraw, rollraw, document.getElementById("rollChart").getContext('2d'))
    } else {
        console.log("update")
        verplaatsingChart.data.datasets[0].data = pitch
        verplaatsingChart.data.datasets[1].data = roll
        verplaatsingChart.update();
        pointsChart.data.datasets[0].data = pitchraw
        pointsChart.data.datasets[1].data = rollraw
        pointsChart.update();
    }
}

function drawChartPoints(DataArray1, DataArray2, ctx) {
	var data = {
            labels: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
        datasets: [{
            label: 'pitch',
            type: "line",
            data:  DataArray1,
            borderColor: 'rgba(44, 62, 80, 1)',
            backgroundColor: 'rgba(44, 62, 80, 0.5)',
            pointRadius: 5,
            pointBackgroundColor: 'rgba(236, 240, 241, 1)',
            order: 1
        }, {
            label: 'roll',
            type: "line",
            data:  DataArray2,
            backgroundColor: 'rgba(52, 152, 219, 0.5)',
            borderColor: 'rgba(52, 152, 219, 1)',
            pointBackgroundColor: 'rgba(236, 240, 241, 1)',
            pointRadius: 5,
            order: 2
        }
    ]};
        
	var options = {
            scales: {
                yAxes : [{
                    ticks : {

                    }
                }]
            }
       
        }

        pointsChart = new Chart(ctx, {
		type: 'line',
		data : data,
		options: options
                
	});
}




function drawChartVerplaatsing(DataArray1, DataArray2, ctx) {
	var data = {
            labels: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
        datasets: [{
            label: 'pitch',
            type: "line",
            data:  DataArray1,
            borderColor: 'rgba(44, 62, 80, 1)',
            backgroundColor: 'rgba(44, 62, 80, 0.5)',
            pointRadius: 5,
            pointBackgroundColor: 'rgba(236, 240, 241, 1)',
            order: 1
        }, {
            label: 'roll',
            type: "line",
            data:  DataArray2,
            backgroundColor: 'rgba(52, 152, 219, 0.5)',
            borderColor: 'rgba(52, 152, 219, 1)',
            pointBackgroundColor: 'rgba(236, 240, 241, 1)',
            pointRadius: 5,
            order: 2
        }
    ]};
        
	var options = {
            scales: {
                yAxes : [{
                    ticks : {
                        max : 40,    
                        min : -40
                    }
                }]
            }
       
        }

        verplaatsingChart = new Chart(ctx, {
		type: 'line',
		data : data,
		options: options
                
	});
}

window.onload = function() {
    fetchInfo()
    loop();
}
