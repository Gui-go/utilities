var data = [
	[300, 150],
	[240, 90],
	[320, 400],
	[120, 120],
	[400, 200],
	[30, 360],
	[250, 200],
	[390, 100]
];

var barchart_width = 800;
var barchart_height = 400;
var padding = 50;

var svg = d3.select('#chart')
	.append('svg')
	.attr('height', barchart_height)
	.attr('width', barchart_width);

// Create scales
var x_scale = d3.scaleLinear()
	.domain([0, d3.max(data, function (d) {  // input domain
		return d[0];
	})])
	.range([padding, barchart_width - padding * 2]);  // output range
var y_scale = d3.scaleLinear()
	.domain([0, d3.max(data, function (d) {
		return d[1];
	})])
	.range([barchart_height - padding, padding]);
var a_scale = d3.scaleSqrt()
.domain([0, d3.max(data, function( d ){
	return d[1];
})])
.range([ 0, 25])

// Create circles
svg.selectAll('circle')
	.data(data)
	.enter()
	.append('circle')
	.attr('cx', function (d) {
		return x_scale(d[0]);
	})
	.attr('cy', function (d) {
		return y_scale(d[1]);
	})
	.attr('r', function (d) {
		//return a_scale((d[0]+d[1])/2);
		return a_scale(d[0]);
	})
	.attr('fill', '#ff6600');  // orange

// Create labels
svg.selectAll('text')
	.data(data)
	.enter()
	.append('text')
	.text(function (d) {
		return d.join(',');
	})
	.attr('x', function (d) {
		return x_scale(d[0]);
	})
	.attr('y', function (d) {
		return y_scale(d[1]);
	});
	//.attr('text-anchor', 'middle');