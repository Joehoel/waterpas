// @ts-nocheck
var count = 0
var count2 = 0
var charttemp
var chartvocht
var chartdruk

function loop() {
	setInterval(function () {
		fetchInfo()
	}, 10 * 100)
}

function fetchInfo() {
	var pitch = []
	var roll = []
	const url = "http://localhost:8000/data"
	fetch(url)
		.then(response => response.json())
		.then(function (data) {
			for (let i = 0; i < data.length; i++) {
				pitch.push(data[i].pitch)
				roll.push(data[i].roll)
			}
			draw(pitch, roll)
		})
}

function draw(pitch, roll) {
	if (count === 0) {
		count = 2
		drawChart(
			pitch,
			document.getElementById("pitchChart").getContext("2d"),
			"Pitch"
		)
		drawChart(
			roll,
			document.getElementById("rollChart").getContext("2d"),
			"Roll"
		)
	} else {
		pitchChart.data.datasets[0].data = pitch
		rollChart.data.datasets[0].data = roll
		pitchChart.update()
		rollChart.update()
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
	}

	var options = {}

	if (count2 === 0) {
		count2++
		pitchChart = new Chart(ctx, {
			type: "line",
			data: data,
			options: options,
		})
	} else if (count2 === 1) {
		count2++
		rollChart = new Chart(ctx, {
			type: "line",
			data: data,
			options: options,
		})
	}
}

window.onload = function () {
	fetchInfo()
	// loop()
}
