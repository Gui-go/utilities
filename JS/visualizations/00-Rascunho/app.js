var var1 = [1, 2, 3, 4, 5, 16, 7, 8, 9, 10, 11, 12, 13, 9, 8, 7, 6, 3]

var width = 500
var height = 500
var padding = 20

var svg = d3.select('#abc')
    .append('svg')
    .attr('width', width)
    .attr('height', height)

var x_scale = d3.scaleBand()
    .domain(d3.range(var1.length))
    .rangeRound([0, width])
    .paddingInner(0.05);

var y_scale = d3.scaleLinear()
    .domain([0, d3.max(var1)/*{ + .2 * d3.max(var1}*/])
    .range([0, height])

svg.selectAll('rect')
    .data(var1)
    .enter()
    .append('rect')
    .attr('x', function (d, i) { return x_scale(i); })
    .attr('y', function (d) { return height - y_scale(d); })
    .attr('width', x_scale.bandwidth())
    .attr('height', function (d) { return y_scale(d); })
    .attr('fill', '#348')

// Event
d3.select('button').on('click', function () {
    var1[0] +=10;
    y_scale.domain([0, d3.max(var1) + 10])
    svg.selectAll('rect')
        .data(var1)
        .transition()
        .delay(function (d, i) { return i / var1.length * 1000; })
        .duration(1600)
        .ease(d3.easeElasticOut)
        .attr('y', function (d) { return height - y_scale(d); });
    //    .attr('height', function (d) { return y_scale(d); });
})