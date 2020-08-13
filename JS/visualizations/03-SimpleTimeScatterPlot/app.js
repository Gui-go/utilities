var data = [
	{ date: '07/01/2017', num: 20},
	{ date: '07/02/2017', num: 30},
	{ date: '07/03/2017', num: 40},
	{ date: '07/04/2017', num: 30},
	{ date: '07/05/2017', num: 20},
	{ date: '07/06/2017', num: 23},
	{ date: '07/07/2017', num: 43},
	{ date: '07/08/2017', num: 29},
	{ date: '07/09/2017', num: 23},
	{ date: '07/10/2017', num: 32},
	{ date: '07/11/2017', num: 44},
	{ date: '07/12/2017', num: 26}
];
var time_parse = d3.timeParse( '%m/%d/%Y' );
var time_format = d3.timeFormat( '%b %e' );

data.forEach(function(e, i){
    data[i].date = time_parse(e.date)
})

var barchart_width = 800;
var barchart_height = 400;
var padding = 50;

var svg = d3.select('#chart')
	.append('svg')
	.attr('height', barchart_height)
	.attr('width', barchart_width);

// Create scales
var x_scale = d3.scaleTime()
    .domain([
        d3.min(data, function( d ){
            return d.date
        }), 
        d3.max(data, function (d) {  // input domain
		return d.date;
	})])
	.range([padding, barchart_width - padding * 2]);  // output range
var y_scale = d3.scaleLinear()
	.domain([0, d3.max(data, function (d) {
		return d.num;
	})])
	.range([barchart_height - padding, padding]);
var a_scale = d3.scaleSqrt()
.domain([0, d3.max(data, function( d ){
	return d.num;
})])
.range([ 0, 25])

// Create circles
svg.selectAll('circle')
	.data(data)
	.enter()
	.append('circle')
	.attr('cx', function (d) {
		return x_scale(d.date);
	})
	.attr('cy', function (d) {
		return y_scale(d.num);
	})
	.attr('r', function (d) {
		return a_scale(d.num);
	})
	.attr('fill', '#ff6600');  // orange

// Create labels
svg.selectAll('text')
	.data(data)
	.enter()
	.append('text')
	.text(function (d) {
		return time_format(d.date);
	})
	.attr('x', function (d) {
		return x_scale(d.date);
	})
	.attr('y', function (d) {
		return y_scale(d.num);
	});
	//.attr('text-anchor', 'middle');