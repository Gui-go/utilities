var data = [
    { key: 0, num: 196, name: "Viegas", curso: "Economia", foto: "https://scontent.ffln8-1.fna.fbcdn.net/v/t1.0-9/43053164_1961252393969359_6215988223403884544_n.jpg?_nc_cat=109&_nc_sid=85a577&_nc_eui2=AeGSiVkjygfGFwUQpUMnlP2ToJzjVJbXk3ignONUlteTeHfqTGHb39lvEhTeBSPM20aUIPz2uYaL8MQ1q-uFI28H&_nc_ohc=03WQBWJq-e4AX_0_xTN&_nc_ht=scontent.ffln8-1.fna&oh=287d961df0baf7ac1bc106434d4978d1&oe=5F0B6AD0" },
    { key: 1, num: 190, name: "Vitor", curso: "Economia", foto: "https://scontent.ffln8-1.fna.fbcdn.net/v/t1.0-9/36587797_1026044507560595_3262882875199979520_n.jpg?_nc_cat=105&_nc_sid=8024bb&_nc_eui2=AeEKPttDbzi0uuCsLgpzAEphI6rT-agGOk4jqtP5qAY6TuPT-Va5tp45sKZUA10RMfUoTYrMGhWaFZbhbKPFBPoe&_nc_ohc=BtpcAfBy8VEAX-_vNRU&_nc_ht=scontent.ffln8-1.fna&oh=be2cebdd5f38dbbe705814b099f5b464&oe=5F0A6233" },
    { key: 2, num: 179, name: "Bruno", curso: "Sistemas", foto: "https://scontent.ffln8-1.fna.fbcdn.net/v/t1.0-9/26229364_1530965150291300_4255880828300032726_n.jpg?_nc_cat=101&_nc_sid=85a577&_nc_eui2=AeEOW4wGDjiXx9nHqoTPa82tBwl2fMLeW4MHCXZ8wt5bg3fp2A1JlWyb0cZ45M614DjPIx0FDvn2TZ9DXUmYaqQu&_nc_ohc=J6kQ2YymDPUAX-wfYMl&_nc_ht=scontent.ffln8-1.fna&oh=a249e277c38ae84f72cf9f5643eb5321&oe=5F0BE61B" },
    { key: 2, num: 175, name: "Thiago SH", curso: "Sistemas", foto: "https://scontent.ffln8-1.fna.fbcdn.net/v/t1.0-9/p960x960/75264994_2572010986198390_5244096231659012096_o.jpg?_nc_cat=108&_nc_sid=85a577&_nc_eui2=AeGG0hEl8krtJa6i8PXeTb6_H0G5v_HSOVkfQbm_8dI5WfkpKI0HFtoZ8KY_u8vYbFiqJgTImkEkHhNh058PaaWZ&_nc_ohc=kURin-ZFFkoAX_jLSAF&_nc_ht=scontent.ffln8-1.fna&_nc_tp=6&oh=d4503d1e44eea635eec45fe307ef253f&oe=5F0C66DB" },
    { key: 2, num: 168, name: "Madeira", curso: "Sistemas", foto: "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/b/b0/JuARaVeInSy.png/revision/latest/top-crop/width/720/height/900?cb=20120722164138" },
    { key: 3, num: 162, name: "Carol", curso: "Economia", foto: "https://scontent.ffln8-1.fna.fbcdn.net/v/t1.0-9/1013198_557011207691222_984507268_n.jpg?_nc_cat=111&_nc_sid=da1649&_nc_eui2=AeEFN0T-NJfYIDwuKb52pMOK4q3uVKddp8Hire5Up12nwe3rfV_iX2o2OHGc_yNSomtQR2RVzsJo0bCM2C_PVbi5&_nc_ohc=TzkKhdVASRMAX8FAyLn&_nc_ht=scontent.ffln8-1.fna&oh=7c86330d0764108f1af64e3ec76ce13e&oe=5F094AAA" }
];

var key = function (d) {
    return d.key;
};

// Create SVG Element
var chart_width = 800;
var chart_height = 400;
var bar_padding = 5;
var svg = d3.select('#chart')
    .append('svg')
    .attr('width', chart_width)
    .attr('height', chart_height);

// Create Scales
// 800 / 15 = 53.33
// 0, 53.33, 106.66
var x_scale = d3.scaleBand()
    .domain(d3.range(data.length))
    .rangeRound([0, chart_width])
    .paddingInner(0.05);
var y_scale = d3.scaleLinear()
    .domain([
        0, d3.max(data, function (d) {
            return d.num;
        })
    ])
    .range([0, chart_height]);

// Bind Data and create bars
svg.selectAll('rect')
    .data(data, key)
    .enter()
    .append('rect')
    .attr('x', function (d, i) {
        return x_scale(i);
    })
    .attr('y', function (d) {
        return chart_height - y_scale(d.num);
    })
    .attr('width', x_scale.bandwidth())
    .attr('height', function (d) {
        return y_scale(d.num);
    })
    .attr('fill', '#002687')
    .on('mouseover', function (d) {
        // console.log(this)
        var x = parseFloat(d3.select(this).attr('x')) + x_scale.bandwidth() / 2;
        var y = parseFloat(d3.select(this).attr('y')) / 2 + chart_height / 2;
        d3.select('#tooltip')
            .style('left', x + 'px')  // posicionamento do tooltip
            .style('top', y + 'px')  // posicionamento do tooltip
            .style('display', 'block')
            //.text(d.name)
            .html(
                "Nome: " + d.name + "<br>" +
                "Altura: " + d.num + " cm" + "<br>" +
                "Curso: " + d.curso + "<br>" + 
                "<img style='max-width:400px;' src='" + d.foto + "'></img>"
            );
            //.html("<p>I'm a tooltip written in HTML</p><img src='https://github.com/holtzy/D3-graph-gallery/blob/master/img/section/ArcSmal.png?raw=true'></img><br>Fancy<br><span style='font-size: 40px;'>Isn't it?</span>")
        d3.select(this)
            .transition()
            .attr('fill', '#0C9CDF');
    })
    .on('mouseout', function () {
        d3.select('#tooltip')
            .style('display', 'none');
        d3.select(this)
            .transition('change_color_back')
            .attr('fill', '#002687');
    });

