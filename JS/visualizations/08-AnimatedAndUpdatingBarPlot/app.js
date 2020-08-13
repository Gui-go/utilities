var data = [6, 20, 21, 14, 2, 30, 7, 16, 25, 5, 11, 28, 10, 26, 9];

// SVG Element
var chart_width = 800;
var chart_height = 400;
var bar_padding = 5;
var svg = d3.select('#chart')
    .append('svg')
    .attr('width', chart_width)
    .attr('height', chart_height);

// x_scale
var x_scale = d3.scaleBand()
    .domain(d3.range(data.length))  // trick to have numerical data as ordinal data
    .rangeRound([0, chart_width])
    .paddingInner(0.09);

// Check
console.log('console.log(d3.range(data.length))')
console.log(d3.range(data.length))       // Array(15) [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, … ]

// y_scale
var y_scale = d3.scaleLinear()
    .domain([0, d3.max(data) + 0.2 * d3.max(data)])
    .range([0, chart_height])

// Check
console.log('d3.max(data) + 0.2 * d3.max(data)')
console.log(d3.max(data) + 0.2 * d3.max(data))

// Bind Data and create bars
svg.selectAll('rect')
    .data(data)
    .enter()
    .append('rect')
    .attr('x', function (d, i) { return x_scale(i); })
    .attr('y', function (d) { return chart_height - y_scale(d); })
    .attr('width', x_scale.bandwidth())
    .attr('height', function (d) { return y_scale(d); })
    .attr('fill', '#00635d');

// Create Labels
svg.selectAll('text')
    .data(data)
    .enter()
    .append('text')
    .text(function (d) { return d; })
    .attr('x', function (d, i) { return x_scale(i) + x_scale.bandwidth() / 2; })
    .attr('y', function (d) { return chart_height - y_scale(d) + 20; })
    .attr('font-size', 14)
    .attr('fill', '#ffffff')
    .attr('text-anchor', 'middle');

// OnClick
d3.select('button').on('click', function () {
    data[5] +=10;
    y_scale.domain([0, d3.max(data) + 10])
    svg.selectAll('rect')
        .data(data)
        .transition()
        .delay(function (d, i) { return i / data.length * 1000; })
        .duration(1600)
        .ease(d3.easeElasticOut)
        .attr('y', function (d) { return chart_height - y_scale(d); })
        .attr('height', function (d) { return y_scale(d); });

    svg.selectAll('text')
        .data(data)
        .transition()
        .delay(function (d, i) { return i / data.length * 1000; })
        .duration(1000)
        .ease(d3.easeElasticOut)
        .text(function (d) { return d; })
        .attr('x', function (d, i) { return x_scale(i) + x_scale.bandwidth() / 2; })
        .attr('y', function (d) { return chart_height - y_scale(d) + 20; })
})