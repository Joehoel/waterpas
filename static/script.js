var count = 0;
var count2 = 0;
var charttemp;
var chartvocht;
var chartdruk;
var pitch = [];
var roll = [];

function loop() {
	setInterval(function () {
		fetchInfo();
	}, 10 * 100);
}

function fetchInfo() {
	const url = "http://localhost:8000/data";
	fetch(url)
		.then(response => response.json())
		.then(function (data) {
			for (let i = 0; i < data.length; i++) {
				pitch.push(data[i].pitch);
				roll.push(data[i].roll);
			}
			draw(pitch, roll);
		});
}

function draw(pitch, roll) {
	if (count === 0) {
		count = 2;
		drawChart(
			pitch,
			document.getElementById("pitchChart").getContext("2d"),
			"Pitch"
		);
		drawChart(
			roll,
			document.getElementById("rollChart").getContext("2d"),
			"Roll"
		);
	} else {
		pitchChart.data.datasets[0].data = pitch;
		rollChart.data.datasets[0].data = roll;
		pitchChart.update();
		rollChart.update();
	}
}

function drawChart(data, ctx, name) {
	var data = {
		labels: Array.from(data.map((_, i) => i + 1)),
		datasets: [
			{
				label: name, // Name the series
				data: data,
				fill: false,
				borderColor: "#2196f3", // Add custom color border (Line)
				backgroundColor: "#2196f3", // Add custom color background (Points and Fill)
				borderWidth: 1, // Specify bar border width
			},
		],
	};

	var options = {};

	if (count2 === 0) {
		count2++;
		pitchChart = new Chart(ctx, {
			type: "line",
			data: data,
			options: options,
		});
	} else if (count2 === 1) {
		count2++;
		rollChart = new Chart(ctx, {
			type: "line",
			data: data,
			options: options,
		});
	}
}

var indicator = $.flightIndicator("#attitude", "attitude", {
	size: 200, // Sets the size in pixels of the indicator (square)
	roll, // Roll angle in degrees for an attitude indicator
	pitch, // Pitch angle in degrees for an attitude indicator
	heading: 0, // Heading angle in degrees for an heading indicator
	vario: 0, // Variometer in 1000 feets/min for the variometer indicator
	airspeed: 0, // Air speed in knots for an air speed indicator
	altitude: 0, // Altitude in feets for an altimeter indicator
	pressure: 1000, // Pressure in hPa for an altimeter indicator
	showBox: true, // Sets if the outer squared box is visible or not (true or false)
	img_directory: "./static/img/", // The directory where the images are saved to
});

window.onload = function () {
	fetchInfo();
	// loop()
};
